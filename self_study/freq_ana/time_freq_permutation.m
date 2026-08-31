% 初始化
clc; clear all;

% 设置路径
cd('/Users/cheng/Desktop/EEG_study/data_for_study/self_study/freq_ana');


%%
% 书接上回，我试试cluster-based permutation聚类置换检验
% 似乎终究绕不开field trip，和eeglab一样的添加方式
% 然后如果用field trip上面的逐点检验就可以不写了


% 首先我们已经有一个整理好的数据ALL了，可以由此进行检验
% 被试；条件；通道；频率；时间
load('./ALL.mat');


%%
% 开始学习fieldtrip代码

% 不过在开始之前，我们仍然可以对通道和时间进行选择以达到ROI的效果
% 然后在构建freq或者timelock结构的时候只保留特定已选定的通道

% 假如我们只做17号通道的，那么只需要按需要取数据子集就好
% 然后通道这个维度也不要压缩，在freq和邻近矩阵输入通道数据的时候就也要调整
% 还有一个遗憾就是，不推荐f检验而推荐t检验两两比较
ALL = ALL(:, 1:2, :, :, :);


%%
% 然后构造fieldtrip的freq结构

% 准备一个胞体，然后每个子胞体是一个空结构体
freq = [];

% 通道信息
% 这里就可以选通道
freq.label = {locs.labels};
% 频域轴
freq.freq = freqs;
% 时间轴
freq.time = times;

% 告诉freq结构被提取的数据维度信息
% 被试条件(rpt)；通道；频率；时间
freq.dimord = 'rpt_chan_freq_time';

% 然后给powspctrm数据
% 这里需要把被试和条件维度给合并，问就是fieldtrip需要
[npar, ncond, nchan, nfreq, ntime] = size(ALL);
ALL = reshape(ALL, [npar * ncond, nchan, nfreq, ntime]);
freq.powspctrm = ALL;


%%
if 1
% 这一节主要是防止以后万一要算空间簇，那么就是构建邻近矩阵
% 首先需要构造一个fieldtrip能读懂的电极位置信息表
locs_changed = [];

% 通道名
locs_changed.label   = {locs.labels};
% 电极坐标
locs_changed.elecpos = [[locs.X]', [locs.Y]', [locs.Z]'];
% 对 EEG 来说一样
locs_changed.chanpos = locs_changed.elecpos;
% 所用单位，需要的时候也能改成cm
locs_changed.unit    = 'mm';


% 然后才能构造邻近矩阵
cfg_neighb = [];

% 这个是怎么算电极们是邻居，这里用的距离，因为我们有locs
cfg_neighb.method = 'distance';
% locs_changed来自EEG.chanlocs的数据
cfg_neighb.elec = locs_changed;


% 最后提取出来邻近矩阵
neighbours = ft_prepare_neighbours(cfg_neighb);
end


%%
% 然后搞设计矩阵
% 设计矩阵其实就是一个表格，第一行是被试信息，第二行是条件或分组信息

% 首先需要准备维度信息
npar;
ncond;

% 然后条件123分别对应rel irr odd
% 默认的都是条件1 - 条件2
cond_rel = 1;
cond_irr = 2;


% 开始定义条件矩阵
design = zeros(2, ncond * npar);

design(1, 1:npar) = 1:npar;  %条件1的被试编号
design(1, (npar + 1):end) = 1:npar;  %条件2的被试编号

% 下面的条件编号同理
design(2, 1:npar) = cond_rel;
design(2, (npar + 1):end) = cond_irr;


%%
% 然后定义统计参数，仍然从创建空结构体开始

cfg = [];

% 蒙特卡洛置换检验，不懂
cfg.method = 'montecarlo';


% 这个是统计量用哪个
% 'indepsamplesF'独立f
% 'depsamplesT'配对样本t；'indepsamplesT'独立样本t
cfg.statistic = 'depsamplesT';
% 单点阈值
cfg.clusteralpha = 0.05;
% 单尾还是双尾检验，
% 1 = 右尾，-1 = 左尾
% t可以双尾；f永远单尾
cfg.tail = 0;


% 使用簇校正
cfg.correctm = 'cluster';
% 簇统计量，这里是求和方法
cfg.clusterstatistic = 'maxsum';
% 簇级别的显著阈值
cfg.alpha = 0.05;
% 簇级别的单双尾
cfg.clustertail = 0;
% 置换次数
cfg.numrandomization = 1000;


% 是否做空间cluster
cfg.minnbchan = 1;

if 1
% 提供邻近矩阵
cfg.neighbours = neighbours;
% 至少两个邻居才能形成簇
cfg.minnbchan  = 2;
end


% 投喂设计矩阵
cfg.design = design;
% unit variable = 被试/观测
cfg.uvar = 1;
% independent variable = 条件/组别
cfg.ivar = 2;


%%
% 准备好上面的统计参数后就可以调用统计函数了
% 时域用ft_timelockstatistics()
% 调用统计函数进行时域分析
output = ft_freqstatistics(cfg, freq);
save('./output_TFR.mat', 'output');


%%
% 然后就可以看结果嘞，关键是结果的数据结构
% 簇的簇级p值，pos前缀，正向结果啦
output.posclusters.prob
% 簇的统计量（t值或F值的对应簇的和）
output.posclusters.clusterstat


% 然后负向性结果的也可以看
% 同样是p值
output.negclusters.prob
% 这个也是统计量
output.negclusters.clusterstat


%%
% 然后是看某个簇的空间时间还有频率分布
% output.posclusterslabelmat是所有簇的编号矩阵
% 比如1是第一大簇，2是第二大以此类推，0就是没有簇
% 然后这就相当于去找效应量排第1的簇，只是按效应大小排序，无关显著性
% output.mask是 显著簇 的掩码矩阵，只有0和1
mask = output.posclusterslabelmat == 1;


% 然后其实我觉得还有个技巧就是用查唯一值的方法去看一共有几个簇
% r里是n_distinct，这里是unique
unique(output.posclusterslabelmat)


% 然后我们去时空定位这个簇的所在，当然还有频率的所在
% ind2sub就是把find的线性索根据size的信息转为多维索引
[chan_id, freq_id, time_id] = ind2sub(size(mask), find(mask));

time_range = output.time(time_id);
freq_range = output.freq(freq_id);
chan_involved = output.label(chan_id);


%%
% 有价值的是怎么去把结果里的显著簇的信息整明白
% 我先用这个工作流将就一下

% 先找到每一个显著簇，先假设0.99为阈值，仅作演示
sig_id = find([output.posclusters.prob] < 0.99);

% 创建并预分配一个table
summary = table(zeros([length(sig_id), 1]), ...
                zeros([length(sig_id), 1]), ...
                zeros([length(sig_id), 1]), ...
                zeros([length(sig_id), 1]), ...
                zeros([length(sig_id), 1]), ...
                zeros([length(sig_id), 1]), ...
                zeros([length(sig_id), 1]), ...
                cell([length(sig_id), 1]), ...
                'VariableNames', {'id','stat','p_value', ...
                                  'freq_min', 'freq_max', ...
                                  'time_min','time_max','chan'});

id = 1;

% 然后就可以利用这个索引定位簇
for ccluster = sig_id
    sig_mask = output.posclusterslabelmat == ccluster;

    % 计算定位索引
    [chan_id, freq_id, time_id] = ind2sub(size(sig_mask), find(sig_mask));

    % 然后每个只取极值表示一下范围就行了
    freq_min = min(output.freq(freq_id));
    freq_max = max(output.freq(freq_id));

    time_min = min(output.time(time_id));
    time_max = max(output.time(time_id));

    % 然后得统计一下重要的数据
    summary.id(ccluster) = id;
    summary.stat(ccluster) = output.posclusters(ccluster).clusterstat;
    summary.p_value(ccluster) = output.posclusters(ccluster).prob;
    summary.freq_min(ccluster) = freq_min;
    summary.freq_max(ccluster) = freq_max;
    summary.time_min(ccluster) = time_min;
    summary.time_max(ccluster) = time_max;

    % 涉及通道比较特殊，一个单元格不好放，干脆这样吧
    chan_id = unique(chan_id);
    summary.chan(ccluster) = {output.label(chan_id)};

    id = id + 1;

end

% 然后就可以check这些玩意了，喜欢哪一个就重点拉出来画图什么的


%%
% 然后就是画图

% 首先是时频图，我仍然更习惯于imagesc
% 因为这个数据没有显著点，所以这里我们就用mask来替代吧
mask = output.posclusterslabelmat == 1;

% 然后我们用Oz的数据
chan_id = find(strcmp(output.label, 'Oz'));
mask = squeeze(mask(chan_id, :, :));
data_plot = squeeze(output.stat(chan_id, :, :));


% 然后开始画时频图
figure;
imagesc(output.time, output.freq, data_plot);
axis xy; colorbar;
% 这个是修改颜色配色
colormap(jet);
% 然后colorbar的数轴规范一下，就是让他对称
clim([-max(abs(data_plot(:))), max(abs(data_plot(:)))]);
hold on;

% 这里主要是要加一个新元素contour，给显著区加边缘线
% [0.5, 0.5]效果一样，就是画一条值为0.5的等高线线，正好是0和1分界线
% 然后贼傻逼的是这里的参数顺序还tm不能乱，傻逼matlab
contour(output.time, ...
        output.freq, ...
        mask, ...
        [0.5, 0.5], ...
        'k-', ...
        'linewidth', 3);
hold off;


% 然后是在显著的地方还得画出来地形图，但是这个我想不难
% 不过我们没有显著数据，所以还是用mask的替代一下
mask = output.posclusterslabelmat == 1;
[chan_id, freq_id, time_id] = ind2sub(size(mask), find(mask));

% 得额外准备一下电极信息
load('./ALL.mat');
chan_id = unique(chan_id);

topo_data = squeeze(mean(output.stat(:, freq_id, time_id), [2, 3]));

% 然后这里也多了一个元素就是emarker2
% 它可以标记一些我们可能感兴趣的电极
% 比如这里就有空间簇，给入通道检索，然后设置格式
figure;
topoplot(topo_data, locs, ...
         'maplimits', 'minmax', ...
         'electrodes', 'on', ...
         'emarker2', {chan_id, '*', 'k', 7});
colorbar;
% 初始化
clc; clear all;

% 设置路径
cd('/Users/cheng/Desktop/EEG_study/data_for_study/self_study/export_data');


%%
% 这里补充一下时域统计分析除了ROI的置换检验

% 读取数据

% 用于循环的准备好变量列表
participant = {
    'umeeg101', 'umeeg102', 'umeeg103', 'umeeg104', ...
    'umeeg105', 'umeeg106', 'umeeg107'
    };

conditions = {
    'rel', 'irr', 'odd'; 
    '201', '202', '203'};

path = '/Users/cheng/Desktop/EEG_study/data_for_study/Chapter 11/data';


% 先给这个循环加个计数功能
count = 0; %用来显示当前所在循环数
total = length(participant) * size(conditions, 2);

% 这次试试预分配
ALL = zeros(length(participant), size(conditions, 2), 70, 512);

for cperson = 1:size(participant, 2)
    for ccond = 1:size(conditions, 2)

        % 数据应该从这里加载
        cEEG = pop_loadset( ...
            'filename', ...
            [participant{cperson} '_11_' conditions{1, ccond} '.set'], ...
            'filepath', path);
        
        % 存储一下个体进度，事件平均叠加
        % ALL的结构 被试；条件；通道；时间
        temp_data = squeeze(mean(cEEG.data(:, :, :), 3));
        ALL(cperson, ccond, :, :) = temp_data;
        clear temp_data;

        % 进度条刷新
        count = count + 1;
        fprintf('current pregress: %.2f %% \n', 100 * count/total)

    end
end

clear ccond conditions count cperson participant path total;


%%
% 开始置换检验

% 然后我们还是按推荐的，两两比较，所以只取两个条件
ALL = ALL(:, 1:2, :, :, :);

% 然后重构数据
[par, cond, chan, time] = size(ALL);
ALL = reshape(ALL, [par * cond, chan, time]);


% 对于ERP数据要建立timelock作为数据结构
timelock = [];

% 数据本体
timelock.avg = ALL;
% 时间轴
timelock.time = cEEG.times;
% 通道名
timelock.label = {cEEG.chanlocs.labels};
% 维度信息
timelock.dimord = 'rpt_chan_time';


%%
% 然后在准备邻近矩阵

% 首先得规整一下电极信息
elec = [];

elec.label = {cEEG.chanlocs.labels};
elec.elecpos = [[cEEG.chanlocs.X]', [cEEG.chanlocs.Y]', [cEEG.chanlocs.Z]'];
elec.chanpos = elec.elecpos;
elec.unit = 'mm';


% 下面才是做邻近矩阵
cfg_neighb = [];
% 计算邻近的方法
cfg_neighb.method = 'distance';
% 提供电极信息
cfg_neighb.elec = elec;


% 然后计算矩阵
neighbours = ft_prepare_neighbours(cfg_neighb);


%%
% 然后就是条件矩阵
% 首先我们有必要的维度信息
par;
cond;

cond_rel = 1;
cond_irr = 2;


% 开始定义矩阵
design = zeros(2, par * cond);

% 首先是第一行，被试行
design(1, 1:end) = [1:par, 1:par];
% 然后是第二行，条件行
design(2, 1:par) = cond_rel;
design(2, (par + 1):end) = cond_irr;


%%
% 然后开始设定统计参数

cfg = [];

% 蒙特卡洛置换检验，不懂
cfg.method = 'montecarlo';


% 这个是统计量用哪个
% 'indepsamplesF'独立f
% 'depsamplesT'配对样本t；'indepsamplesT'独立样本t
cfg.statistic = 'depsamplesT';
% 单点阈值
cfg.clusteralpha = 0.001;
% 单尾还是双尾检验，0 = 双尾；1 = 单尾
% t可以双尾；f永远单尾
cfg.tail = 1;


% 使用簇校正
cfg.correctm = 'cluster';
% 簇统计量，这里是求和方法
cfg.clusterstatistic = 'maxsum';
% 簇级别的显著阈值
cfg.alpha = 0.01;
% 簇级别的单双尾
cfg.clustertail = 1;
% 置换次数
cfg.numrandomization = 1000;


% 提供邻近矩阵
cfg.neighbours = neighbours;
% 至少n个邻居才能形成簇，为0时就是干脆不做空间簇了
cfg.minnbchan  = 2;


% 投喂设计矩阵
cfg.design = design;
% unit variable = 被试/观测
cfg.uvar = 1;
% independent variable = 条件/组别
cfg.ivar = 2;


%%
% 然后开始进行统计
output = ft_timelockstatistics(cfg, timelock);

% 清一下变量
locs = cEEG.chanlocs;
clear cEEG cfg cfg_neighb cond_irr cond_rel design elec neighbours timelock;

%%
% 然后就是查看统计结果
sig_id = find([output.posclusters.prob] < 0.05);

summary = table(...
                zeros([length(sig_id), 1]), ...
                zeros([length(sig_id), 1]), ...
                zeros([length(sig_id), 1]), ...
                zeros([length(sig_id), 1]), ...
                cell([length(sig_id), 1]), ...
                'variablenames', {'p_value', 'stat', ...
                                  'time_min', 'time_max', ...
                                  'chan'});

for ccluster = sig_id
    mask = output.posclusterslabelmat == ccluster;
    [chan_id, time_id] = ind2sub(size(mask), find(mask));

    time_range = output.time(time_id);
    time_min = min(time_range);
    time_max = max(time_range);

    chan_id = unique(chan_id);
    chan_involved = {output.label(chan_id)};

    % 记录统计结果
    summary.p_value(ccluster) = output.posclusters(sig_id).prob;
    summary.stat(ccluster) = output.posclusters(sig_id).clusterstat;
    summary.time_min(ccluster) = time_min;
    summary.time_max(ccluster) = time_max;
    summary.chan(ccluster) = chan_involved;
end

clear sig_id chan_id chan_involved ccluster time_id time_min time_max time_range;


%%
% 绘制波形图（毕竟只是时域信息）和地形图
ALL = reshape(ALL, [par, cond, chan, time]);
group_rel = squeeze(mean(ALL(:, 1, :, :), 1));
group_irr = squeeze(mean(ALL(:, 2, :, :), 1));

% 然后我们只用第3大簇的时间，它的时间窗像p3
time_min = summary.time_min(3);
time_max = summary.time_max(3);


% 然后我们只用37号电极举例子
% 画图
figure; hold on;

% 根据振幅手动设定y轴
ylim([-2, 2]);

% 然后用patch显著阴影(实际就是画多边形）
% 头俩参数分别是x和y的顶点坐标，依次相连哈
% 第三个是RGB颜色
patch([time_min, time_min, time_max, time_max], ...
      [-2, 2, 2, -2], ...
      [0.8, 0.8, 0.8], ...
      'edgecolor', 'none', ...
      'facealpha', '0.6');

% 然后是两个啵啵😘，保存为变量，后面指定图例的时候用
p1 = plot(output.time, ...
          group_rel(37, :), ...
          'b', ...
          'linewidth', 3);
p2 = plot(output.time, ...
          group_irr(37, :), ...
          'r', ...
          'linewidth', 3);

% 一些线
yline(0, 'k--', 'LineWidth', 1.5);
xline(0, 'k--', 'LineWidth', 1.5);
% 图例
legend([p1, p2], {'relevant', 'irrelevant'});

hold off;

clear time_max time_min p1 p2 mask group_irr group_rel;


% 然后是tmd地形图
% 然后还是用第3个簇的呗，那个看起来像是p3
% 首先找出时间定位
min_id = find(output.time == summary.time_min(1));
max_id = find(output.time == summary.time_max(1));

% 然后空间簇整一下
chan_id = find(ismember(output.label, summary.chan{1}));


data_plot = ALL(:, 1:2, :, min_id:max_id);
data_plot = squeeze(mean(data_plot, [1, 4]));


% 然后画这个地形图
for ccond = 1:size(data_plot, 1)
    subplot(1, 2, ccond);

    topoplot(squeeze(data_plot(ccond, :)), ...
             locs, ...
             'maplimits', 'absmax', ...
             'electrodes', 'on');
end

clear ans ccond chan_id data_plot locs max_id min_id;


% 然后这个基于簇的置换检验有个问题
% 就是如果你观察一下最大的那个显著簇，你会发现它的持续时间大得离谱
% 这是可能因为空间簇的阈值低，导致一个通道的显著区很快结束后立马又被另一个时空邻近的通道的显著区给续上了
% 然后击鼓传花，最后变成了一个巨型簇，当然，**这些都只是可能**


% 这个问题的解决方法可以是提高空间簇的阈值，但是在该数据集上稍微提一点就虚无假设了
% 还有就是在结果汇报上可以明确说明这个可能是一种“跳跃簇”，并配合通道时间图
% "该簇可能反映了两个时间上分离但空间上部分重叠的神经过程，需谨慎解读为单一连续效应"

% 通道时间图，代码形式上和时频图一样
% 这次就是回头看看第一个那个巨型簇
mask = output.posclusterslabelmat == 1;
data_plot = output.stat;

figure;
imagesc(output.time, 1:numel(output.label), data_plot);
axis xy; colorbar; clim([-max(abs(data_plot(:))), max(abs(data_plot(:)))]);
hold on;

contour(output.time, ...
        1:numel(output.label),...
        mask, ...
        [0.5, 0.5], ...
        'k', ...
        'linewidth', 3);
hold off;


% 但是这张图还是不能很直观看出来是否接力
% 所以试试时间*显著通道数的可视化看看
% 计算显著通道数
sig_chan_n = sum(mask, 1);

% 绘制时间与显著通道数的关系
figure;
plot(output.time, sig_chan_n, 'k', 'LineWidth', 2);
xlabel('time');
ylabel('number of sig channels');
grid on;


% 所以仍然不懂到底是咋回事，果然提前选好ROI太重要了。
% 这个脚本仅仅是代码形式上提供一个未来可用的置换检验的工作流
% 初始化
clc; clear all;

% 设置路径
cd('/Users/cheng/Desktop/EEG_study/data_for_study/self_study/plot_EEG');


%%
% 加载数据先

participant = {'101', '102', '103', '104', '105', '106', '107'};
condition = {'irr', 'rel'};
path = '/Users/cheng/Desktop/EEG_study/data_for_study/Chapter 10/data';

EEG = pop_loadset( ...
    'filename', ...
    ['umeeg', participant{1}, '_11_', condition{1}, '.set'], ...
    'filepath', ...
    path);


%%
% 然后它后面初期的内容有点像我那个matlab的练习
% 去结构体查channel location然后
% 按照维度平均以后plot

figure;
plot(EEG.times, mean(EEG.data(25, :, :), 3), ...
    'b', 'linewidth', 4);


%%

participant = {'101', '102', '103', '104', '105', '106', '107'};
condition = {'irr', 'rel'};
path = '/Users/cheng/Desktop/EEG_study/data_for_study/Chapter 10/data';

% 问题是我是想知道Study的图咋画
% 首先需要创建空列表，结构和EEG差不多，但是多一个维度是被试号
% 然后假如我们就画俩通道的信息, 第三个维度2
% 还有就是我们要叠加平均，所以最后那个512就是这样来的
% 最后我们有俩conditions，第二个维度那个2就是这样来的
ERP = zeros(7, 2, 2, 512);


% 下面我们才可以开始准备画图用的数据

for cpeople = 1:size(ERP, 1)
    for ccondition = 1:size(ERP, 2)

        % 然后先加载数据，每个人每个条件的数据
        EEG = pop_loadset( ...
        'filename', ...
        ['umeeg', participant{cpeople}, '_11_', condition{ccondition}, '.set'], ...
        'filepath', ...
        path);


        % 但是有个问题就是我们的感兴趣channel是Pz和Cz
        % 然而这七个被试用的设备不一样，然后他们对应这俩通道的编号也不一样
        % 所以得先提前查出来通道编号并使用另一个list记录
        % cell array 不能用 == 来比较
        % strcmp({}, '')就是看两者是否相等，就是字符细胞的find()
        chan(1) = find(strcmp({EEG.chanlocs.labels}, 'Cz'));
        chan(2) = find(strcmp({EEG.chanlocs.labels}, 'Pz'));

        % 然后是选择通道，把叠加平均的数据记录到list的对应位置
        for cchan = 1:size(ERP, 3)

            ERP(cpeople, ccondition, cchan, :) = mean(EEG.data(chan(cchan), :, :), 3);

        end
    end
end


%%
% 以上是统计特定通道特定条件的叠加平均，然后把所有被试都纳入记录
% 下面就该是利用我们准备好的数据进行画图了
% 现在是ERP是每个被试不同通道和条件下已经按照epoch平均了的数据
% 再可视化就是进一步按照条件进一步平均

% 这样它能自动在同一图中比较俩条件
Cz_mean = squeeze(mean(ERP(:, :, 1, :), 1));

plot(EEG.times, Cz_mean)

%或者这样一样的效果
Cz_irr_mean = squeeze(mean(ERP(:, 1, 1, :), 1));
Cz_rel_mean = squeeze(mean(ERP(:, 2, 1, :), 1));

figure;
plot(EEG.times, Cz_irr_mean);
hold on
plot(EEG.times, Cz_rel_mean);
hold off


%%
% subplot就更不用说了，这次加入俩通道
Cz_mean = squeeze(mean(ERP(:, :, 1, :), 1));
Pz_mean = squeeze(mean(ERP(:, :, 2, :), 1));


subplot(2, 1, 1);
plot(EEG.times, Cz_mean);
title('Cz mean potential');
xline(0, '--k', 'LineWidth', 1.5);  % 那条虚线
% plot([0 0], ylim, '--k', 'LineWidth', 1.5) 旧版这样画虚线，别忘了hold on
legend({'irrelevant', 'relevant'});  % 图例最后画
subplot(2, 1, 2);
plot(EEG.times, Pz_mean);
title('Pz mean potential');
xline(0, '--k', 'LineWidth', 1.5);


%%
% 然后波形图在r脚本里似乎搞了
% 哦R脚本没有保存，反正就是提出来数据以后就能画，这个不难
% matlab里也不难
% 反正先准备一下组水平的数据

% eeglab

file_path = '/Users/cheng/Desktop/EEG_study/data_for_study/Chapter 11/data/';

participants = {'umeeg101', 'umeeg102', 'umeeg103', 'umeeg104', ...
                'umeeg105', 'umeeg106', 'umeeg107'};

cond = {'rel', 'irr', 'odd'; ...
        201, 202, 203};

count = 0;
total = length(participants) * size(cond, 2);

% 整一个mat来把数据提取出来后面画图或者什么时候用
% 这个mat保留了多维度特征同时没有表头，跟用在R里的那个不太一样
for par = 1:length(participants)
    for ccond = 1:size(cond, 2)

        % 首先加载数据
        EEG = pop_loadset( ...
            'filename', ...
            [participants{par} '_11_' cond{1, ccond}, '.set'], ...
            'filepath', ...
            file_path);

        % 然后保存，先事件平均
        % 被试，条件，通道，时间，这四个维度
        ALLEEG(par, ccond, :, :) = mean(EEG.data, 3);

        % 计数君
        count = count + 1;
        fprintf('current pregress: %.2f %% \n', 100 * count/total);
    end
end


% 首先是组水平的波形图
% 首先先挑选出来通道，假如是Cz
chan_number = find(strcmp({EEG.chanlocs.labels}, 'Cz'));

% 然后获得组水平的数据，顺便把通道取了
wave_data = squeeze(mean(ALLEEG(:, :, chan_number,:), 1));


% 画图吧就，组水平的
figure;
plot(EEG.times, wave_data);
xlabel('time');
ylabel('potential');
title('Cz');
legend(cond{1, :});


% 最主要的是我想代码画地形图
% 地形图用来找数据驱动ROI的时候可以用
% 但是GUI里面不让一次画一堆


% 然后这次我们不区分条件
% 同时还得整出来组水平的
% 这里就是一次性把前两个维度给平均掉
cEEG = squeeze(mean(ALLEEG, [1 2]));


% 假如我们要探索的大时间窗是0-600ms，看每100ms的地形变化
total = length(0:100:500);  %用这个结果看一共画几个图
count = 0;  %用这个计数加指引排版


for i = 0:100:500
    % 准备时间内的数据
    % 然后别忘了还得把时间维度给平均压缩
    segment = find(EEG.times > i & EEG.times < i + 100);
    topo_data = squeeze(mean(cEEG(:, segment), 2));

    % 准备画图，提前想好图的排版
    count = count + 1;
    subplot(2, 3, count);
 
    % 开始画地形图
    % maplimits参数管数值的颜色范围，
    % 时域信息和CIA的地形图为了保证极性对称用absmax
    % 时频分析的地形图不用保证对称，用maxmin

    % electrodes 一般都是on
    % 还有个style参数直接用的默认，这里没写
    topoplot(topo_data, EEG.chanlocs, ...
             'maplimits', 'absmax', ...
             'electrodes', 'on');
    title(sprintf('topograph %d - %d ms', ...
                  i, i + 100))
    colorbar;
end


% 然后还有就是不同条件的地形图比较
% 同样准备数据，然后这次我们假如已经知道了目标时间窗为250 - 350ms
TOI = find(EEG.times > 250 & EEG.times < 350);

% 然后获得组水平数据，顺带压缩时间，反正这次都知道TOI
cEEG = squeeze(mean(ALLEEG(:, :, :, TOI), [1 4]));

% 然后准备一下条件list
cond = {'rel', 'irr', 'odd'; ...
        201, 202, 203};

% 准备循环
for i = 1:size(cond, 2)
    topo_data = cEEG(i, :);

    % 画地形图
    subplot(1, 3, i);

    % 和刚刚不一样的是，洪城课题组建议跨条件比较的时候颜色范围最好统一
    topoplot(topo_data, EEG.chanlocs, ...
             'maplimits', [-3 3], ...
             'electrodes', 'on');
    colorbar;
    title(cond{1, i});
end
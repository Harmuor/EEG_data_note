% eeglab
clear all; clc;

cd('/Users/cheng/Desktop/EEG_study/data_for_study/self_study/freq_ana');

%%
% 需要注意的是stft时频分析的数据时间窗和spape那个有冲突
% 数据时间窗如果要用于时频分析，洪城课题组留了[-1, 2]
% 但是spape的实验设计并没有考虑这个玩意，只留了[-0.2, 0.8]

% 数据和封装函数sub_stft()来源于洪城课题组


%%
% 这里是小波变换，似乎更为流行
% 它的滑动窗口的长度是可变的

% 这里先用一个被试的一个条件的一个通道数据试一试
EEG = pop_loadset('filename', ...
                  'umeeg102_11_rel.set', ...
                  'filepath', ...
                  '/Users/cheng/Desktop/EEG_study/data_for_study/Chapter 11/data');

% 然后就是对其中一个通道做小波变换
% ersp就是一个频率 * 时间的功率数据
[ersp, itc, powbase, times, freqs] = ...
newtimef(EEG.data(1, :, :), ...
         EEG.pnts, ...
         [EEG.xmin, EEG.xmax] * 1000, ...
         EEG.srate, ...
         [1, 0.5], ...
         'nfreqs', 50, ...
         'ntimesout', 100, ...
         'freqs', [4, 80], ...
         'baseline', [EEG.xmin * 1000, 0], ...
         'plotersp', 'off', ...
         'plotitc', 'off');

% 试着画图
imagesc(times, freqs, ersp);
axis xy;  % 这个是y轴坐标轴反转
colorbar;


%%
% 下面开始组水平的不同条件绘图
% 还是准备首先加载数据
% 这个计算太耗时间而且我的mac只是丐版air，所以先拿6个被试跑一跑算了
participants = {'umeeg101', 'umeeg102', 'umeeg103', 'umeeg104', ...
                'umeeg105', 'umeeg106'};

cond = {'rel', 'irr', 'odd'};


% 再写个计数君
count = 0;

% 需要写一个总数，这里我知道每个条件的试次数量是不一定的，但是至少输出的数据结构是一定的
% 就是2个被试，3种条件，70个通道，100个频率点，100个时间点
total = 3 * 3 * 70;


% 正确的时频分析逻辑仍然是先按通道将数据傅立叶变换，但是不要叠加
% 把一个个体所有数据傅立叶变换以后再叠加，最后汇总为一个组的频域数据
for cpar = 1:length(participants)
    for ccond = 1:length(cond)

        % 加载数据
        EEG = pop_loadset('filename', ...
                          [participants{cpar} '_11_' cond{ccond} '.set'], ...
                          'filepath', ...
                          '/Users/cheng/Desktop/EEG_study/data_for_study/Chapter 11/data');

        % 对每个通道做小波变换然后叠加平均为一个被试某个条件的
        for cchan = 1:length(EEG.chanlocs)
            [temp(cchan, :, :), ~, ~, temp_t, temp_f] = ...
                newtimef(EEG.data(cchan, :, :), ...
                         EEG.pnts, ...
                         [EEG.xmin, EEG.xmax] * 1000, ...
                         EEG.srate, ...
                         [1, 0.5], ...
                         'freqs', [4, 30], ...
                         'nfreqs', 80, ...
                         'ntimesout', 300, ...
                         'baseline', [EEG.xmin * 1000, 0], ...
                         'plotersp', 'off', ...
                         'plotitc', 'off' ...
                         );

            % 这里用条件控制只保存一次时间和频率轴
            if cchan == 1 && ccond == 1 && cpar == 1
                times = temp_t; freqs = temp_f;
            end

            % 清除缓存
            clear temp_t temp_f;

            % 然后计数
            count = count + 1;
            fprintf('current pregress: %.2f %% \n', 100 * count / total)
            drawnow;   % 强制刷新
        end

        % 最后用ALL存储数据：被试；条件；通道；频率；时间
        ALL(cpar, ccond, :, :, :) = temp;
        clear temp;
    end
end

locs = EEG.chanlocs;

% 保存一下数据万一以后用
save('ALL.mat', 'ALL', 'times', 'freqs', 'locs');


%%
% 终于就是组平均了

group = squeeze(mean(ALL, 1));

% 然后画时频图
% colorbar这个咋统一是个艺术
subplot(311);
imagesc(times, freqs, squeeze(group(1, 1, :, :)));
title('relevant condition')
xlabel('times');
ylabel('dB')
axis xy;
colorbar

subplot(312);
imagesc(times, freqs, squeeze(group(2, 1, :, :)));
xlabel('times');
ylabel('dB')
title('irrelevant condition')
axis xy;
colorbar

subplot(313);
imagesc(times, freqs, squeeze(group(3, 1, :, :)));
xlabel('times');
ylabel('dB')
title('oddball condition')
axis xy;
colorbar


%%
% 然后画地形图

id_delta = find(freqs >= 4 & freqs <= 7);
id_time = find(times >= 250 & times < 350);

topo_data = squeeze(mean(group(1, :, id_delta, id_time), [3, 4]));

figure;
topoplot(topo_data, locs, ...
         'electrodes', 'on', ...
         'maplimits', [-1, 1]);
colorbar;
title('Rel condition: 4–7 Hz, 250–350 ms');


%%
% 然后就涉及统计分析了
% ALL的结构再回顾一下 被试；条件；通道；频率；时间

% 然后我看liu zhenghao的统计分析也是逐点比较但是我估计他应该有一些矫正方法
% 果然，cluster-based permutation test，成簇检验，用的fieldtrip

%%
% 首先先用俩情况的，学一下逐点的t检验
% 对于两种情况下每一个时频点进行逐点t检验

for cfreq = 1:size(ALL, 4)
    for ctime = 1:size(ALL, 5)
        % 准备两组数据
        data_1 = squeeze(ALL(:, 1, 17, cfreq, ctime));
        data_2 = squeeze(ALL(:, 2, 17, cfreq, ctime));

        % 然后收集p值和t分数
        % ttest2是配对样本t，普通的就是ttest
        [~, temp_p, ~, temp_t] = ...
            ttest2(data_1, data_2);

        p_value(cfreq, ctime) = temp_p;
        t_value(cfreq, ctime) = temp_t.tstat;
    end
end

clear temp_p temp_t data_1 data_2 cfreq ctime;


% 如果是（单因素）方差分析就是
for cfreq = 1:size(ALL, 4)
    for ctime = 1:size(ALL, 5)

        % 这次把三种条件全带上
        % 然后其实就是一个实实在在的表格，行是观测，列是组
        data_3 = squeeze(ALL(:, :, 17, cfreq, ctime));

        % 就直接单因素anova就行，off是关闭画图
        % [~, ans2] = anova1(data_3, {'rel', 'irr', 'odd'}, 'off');
        [~, ans2] = anova1(data_3, [], 'off');       

        % 存答案
        f_value(cfreq, ctime) = ans2{2, 5};
        p_value(cfreq, ctime) = ans2{2, 6};
    end
end

clear ans2 data_3 cfreq ctime;


% 然后洪城课题组用了fdr矫正，但还是逐点的思想，这里用t检验做例子
% 据说相当严格，不过你就可以用masked那个变量画新的图
[p_fdr, p_masked] = fdr(p_value, 0.05);


% 画图
imagesc(times, freqs, p_value);
axis xy;
colorbar;
caxis([0, 0.05]);  %这一步主要是凸显显著的数据

% 或者也可以用t分数画图
% 我知道很丑
imagesc(times, freqs, t_value);
axis xy;
colorbar;
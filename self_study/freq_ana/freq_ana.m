% 初始化
clc; clear all;

% 设置路径
cd('/Users/cheng/Desktop/EEG_study/data_for_study/self_study/freq_ana');


%%
% 这里首先是之前频域分析里面的内容，思路看rmarkdown笔记
% 我们直接看怎么应用到eeglab数据里
% 一般频域分析都是用在静息态数据里的
% 这里就假设cond维度记录的不是条件，而是分段

% eeglab

% 首先加载数据
participants = {'umeeg101', 'umeeg102', 'umeeg103', 'umeeg104', ...
                'umeeg105', 'umeeg106', 'umeeg107'};

cond = {'rel', 'irr', 'odd'};


% 正确的fft逻辑是先按通道将数据傅立叶变换，但是不要叠加
% 把一个个体所有数据傅立叶变换以后再叠加，最后汇总为一个组的频域数据
for cpar = 1:length(participants)
    for ccond = 1:length(cond)

        % 加载数据
        EEG = pop_loadset('filename', ...
                          [participants{cpar} '_11_' cond{ccond} '.set'], ...
                          'filepath', ...
                          '/Users/cheng/Desktop/EEG_study/data_for_study/Chapter 11/data');

        % 然后每个数据都是通道 * 时间 * 试次
        % 原封不动fft，不要叠加
        for cepoch = 1:size(EEG.data, 3)
            for cchan = 1:size(EEG.data, 1)

                % 先准备一个傅立叶变化的“重采样”，这个是优化计算的步骤
                % 这个主要是找到离本来采样率最近的2的次幂数
                NFFT = 2^nextpow2(EEG.srate);

                % 开始fft，用一个临时变量存储每一个通道的数据
                temp = fft(EEG.data(cchan, :, cepoch), NFFT);
                temp = abs(temp);

                % 然后记录一下一个个体的振幅
                cEEG(cchan, :, cepoch) = temp .* 2 ./ length(temp);
            end
        end

        % 保存数据，这个时候再平均叠加
        % 被试；条件；通道；频率
        ALL(cpar, ccond, :, :) = squeeze(mean(cEEG, 3));

        % 清除缓存
        clear temp; clear cEEG;
    end
end

disp('done')


% 计算频率list
% NFFT = size(ALL, 4)都是fft的采样率
% 其实这样也可以
% freq_1 = linspace(0, EEG.srate, NFFT);
freq = (0:(NFFT - 1)) * EEG.srate / NFFT;


% 然后看一看前50个频率在第一个通道的组水平振幅
% 无视条件信息，仅为代码演示方便
% 其他的功率什么的套公式就是
group = squeeze(mean(ALL, [1 2]));

figure;
plot(freq(1:50), group(1, 1:50));


% 当然也可以直接看整个Nyquist频率
% 这里仍然用第一个通道作为演示
group = squeeze(mean(ALL, [1 2]));

figure;
nyquist = NFFT / 2 + 1;
plot(freq(1:nyquist), group(1, 1:nyquist));

%%
% 然后用这个频域信息，我用的是振幅，画地形图
group;

count = 0;

for i = 0:5:35
    count = count + 1;
    segment = find(freq >= i & freq <= i + 5);
    plot_amplitude = squeeze(mean(group(:, segment), 2));
    subplot(2, 4, count)

    % 然后maplimits这个参数怎么用还是没有搞懂
    topoplot(plot_amplitude, EEG.chanlocs, ...
             'electrodes', 'on', ...
             'maplimits', 'absmax');
    title([num2str(freq(segment(1))) '-' num2str(freq(segment(end))) ' Hz'])
    colorbar;
end


%%
% 频域统计分析和时域的统计分析在代码形式上一致
% 不过要是想在r里用的舒服点估计还是得弄出个带表头的数据
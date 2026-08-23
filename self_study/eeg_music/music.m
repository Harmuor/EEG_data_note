% 初始化
clc; clear all;

% 设置路径
cd('/Users/cheng/Desktop/EEG_study/data_for_study/self_study/eeg_music');


%%
x = linspace(0, 2 * pi, 8192);  %这里的2pi就是一个音的持续时间
y = sin(440 * x);

plot(x, y)

% sound()函数里Fs = 采样率，nBits无需多言
% 采样率影响不大，主要是频率
sound(y)

% 使用十二平均率表可以通过调整频率来实现音符变换
% 一个八度分为8个单位，频率间隔（倍率？）为2^(1/12)
% 比如C调的do音可以被规定为Fs * 2^(1/12 * 0)，然后高一度的do就是Fs * 2^(1/12 * 12)


%%
% 试试怎么弄出来一段音乐
fs = 8192;  %使用matlab默认采样率
duration = 0.5;  %每个音发500ms
t = linspace(0, duration, fs * duration);  %每个音的采样list


% 准备一下所用的频率
% 小星星是1 1 5 5 6 6 5来着
p_l = 440 * [2^(0/12), 2^(0/12), 2^(7/12), 2^(7/12), ...
             2^(9/12), 2^(9/12), 2^(7/12)];


for i = 1:length(p_l)
    % 虽然还是不明白为什么要带2pi
    % 说是让声音回归周期
    wave = sin(2 * pi * p_l(i) * t);
    sound(wave, fs);
    pause(0.5);  %每放一个音中间暂停0.1秒
    subplot(2, 4, i);
    plot(t, wave)
end


%%
% 试试 *Call of Slience*
% 首先这个是三个八度的音符频率
% 基准频率100比较有感觉诶
p_l = 100 * [2^(-9/12), 2^(-7/12), 2^(-5/12), 2^(-4/12), 2^(-2/12), 2^(0/12), 2^(2/12)];
p_m = 100 * [2^(3/12), 2^(5/12), 2^(7/12), 2^(8/12), 2^(10/12), 2^(12/12), 2^(14/12)];
p_h = 100 * [2^(15/12), 2^(17/12), 2^(19/12), 2^(20/12), 2^(22/12), 2^(24/12), 2^(26/12)];

% 然后准备一下谱子
tone = [p_h(3), p_h(2), p_h(2), p_h(1), p_h(1), p_h(5), p_h(1), p_h(1), p_m(7), p_h(1), p_h(1), ...
        1, ...
        p_h(3), p_h(2), p_h(2), p_h(1), p_m(5), p_m(5), p_h(3), p_h(2), p_h(2), p_h(3), p_h(1), ...
        1, ...
        p_h(3), p_h(2), p_h(2), p_h(1), p_h(1), p_h(5), p_h(5), p_h(5), p_h(2), p_h(2), p_h(1), ...
        1, ...
        p_m(6), p_h(1), p_h(2), 1, p_h(2), p_h(1), p_h(2), p_h(3), p_h(2), p_h(2), p_h(2), p_h(1), ...
        1, ...
        p_h(1), p_m(7), p_m(3), p_m(6), p_m(6), 1, p_h(1), p_m(7), p_m(3), p_m(1), ...
        1, ...
        p_h(1), p_m(7), p_h(1), p_h(2), 1, p_h(3), 1, p_h(1), p_m(7)];

% 然后准备一下时间轴
fs = 8000;
duration = 0.6;
t = linspace(0, duration, duration * fs);

% 准备一个list用来拼接音乐
all_wave = [];

% 开始tm播放！
for i = 1:length(tone)
    wave = sin(2 * pi * tone(i) * t);
    sound(wave, fs);
    pause(0.6);
    all_wave = [all_wave, wave];  %这个是拼接的操作
end

audiowrite('call of slience.mp3', all_wave, fs);


%%
% 怎么把脑电数据变成音乐来着嘞

% 如果每个epoch都是1秒，采样率是512，也就是说一个epoch只需要一个y值来代表
% 就先弄一个被试的试试吧
% eeglab
EEG = pop_loadset( ...
    './umeeg101_10_Pruned_with_ICA.set' ...
    );

% 假如每个epoch是提供一个音节的频率
% 然后提取Cz通道的数据，拉伸一下再
chan = find(strcmp({EEG.chanlocs.labels}, 'Cz'));
data = EEG.data(chan, :);

% 然后准备一下采样率和时间轴什么的
% 设定每半秒一个音符就得准备一个半秒的时间序列
fs = EEG.srate;
win = 0.5;  % 每半秒一个音符

% 这个sample是每半秒里的数据点数量
% 构建for loop的时候用作步长
samples = win * fs;

% 然后这是播放的采样率
fs_audio = 8000; 


% 可以用来保存音符
% all_wave = [];


for i = 1:samples:200 * samples

    % 然后回到我们的通道数据，每半秒的时间序列取一个段
    segment = data(i:i+samples - 1);

    % 时域信息转为频域信息
    % 虽然fft不改变数据结构，但是改变意义
    % 采样率是fs，数据点数量是n，然后索引是k(0:n-1)
    % 然后第k点的频率freq = k * fs/n
    Y = fft(segment);

    % 提取出来振幅，然后抛弃相位信息
    P = abs(Y);
    P = 2 .* P ./ length(P);

    % 这个freqs变量类似于时域信息里的EEG.times
    % 用刚刚那个公式算出来
    freqs = (0:length(P) - 1) * fs / length(P);

    % 然后就是把特定频率对应的索引找出来
    idx = find(freqs >= 7 & freqs <= 12);

    % 然后把这个band的最大功率点找出来
    % 然后再找出来这个最大功率点对应的freq给取出来备用就好
    [~, max_idx] = max(P(idx));
    eeg_freq = freqs(idx(max_idx));


    % 映射到音乐频率，为什么这样洒家不知道
    % 使用基准频率
    music_freq = 100 * 2^(eeg_freq / 12);

    % 生成声音，和时间轴
    t = linspace(0, win, win * fs_audio);
    wave = sin(2 * pi * music_freq * t);

    sound(wave, fs_audio);
    pause(win);

    % 还是拼接的操作
    % all_wave = [all_wave, wave];
end


% 这里可以保存
% audiowrite('alpha.mp3', all_wave, fs_audio)


%%
% 弄个群体的
% 感觉也就是多了一个数据平均的过程呗
% 感觉可以多弄出一个循环来进行这个操作
% 然后后续也是fft什么的
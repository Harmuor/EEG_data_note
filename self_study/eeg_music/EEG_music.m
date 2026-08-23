% 初始化
clc; clear all;

% 设置路径
cd('/Users/cheng/Desktop/EEG_study/data_for_study/self_study/eeg_music');


% first load a epoched dataset
% I used umeeg101 for this
EEG = pop_loadset( ...
    'filename', 'umeeg101_10_Pruned_with_ICA.set', ...
    'filepath', '.');

% this command will play the sound composed by the channel 5 and 8, all
% timepoints of the first epoch
sound(EEG.data([5 18], :, 1));

% if we have loaded a study set, we can use the command below
sound(ALLEEG(1).data([5 18],:,1))
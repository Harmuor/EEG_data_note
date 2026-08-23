% 初始化
clc; clear all;

% 设置路径
cd('/Users/cheng/Desktop/EEG_study/data_for_study/self_study/batch_preprocess');


%%
protocol = {
    'umeeg101', '.vhdr';
    'umeeg103', '.vhdr';
};


%%
% 首先就是插值或者删除坏道之前的都能代码化
for i = 1:size(protocol, 1)

    % 加载数据
    EEG = pop_loadbv('.', [protocol{i, 1}, protocol{i, 2}]);

    % 重采样
    EEG = pop_resample(EEG, 512);

    % 节选，首先确定第一个和最后一个marker的时间
    % 但是我不知道何意味
    first_marker = EEG.event(3).latency / EEG.srate;
    last_marker = EEG.event(end).latency / EEG.srate;
    EEG = pop_select( EEG, ...
        'time', [first_marker - 20, last_marker + 20]);

    % 滤波
    EEG = pop_eegfiltnew(EEG, 'hicutoff', 80, 'locutoff', 0.2);
    EEG = pop_eegfiltnew(EEG, 'hicutoff', 46, 'locutoff', 54, 'revfilt', 1);

    % 分段和基线
    EEG = pop_epoch(EEG, {'201', '202', '203'}, [-0.2, 0.8]);
    EEG = pop_rmbase(EEG, [EEG.xmin, 0]);

    % 先存一下数据
    pop_saveset( ...
        EEG, ...
        ['./' protocol{i, 1} '_epoched.set']);
end


%%
% 删除坏道和插值，必须手动并且登记相关信息到list，这样批量跑ica的时候用得着


%%
% 假如某个被试有坏道然后我们进行插值，那么我们用这个list记一下
% 最后一列是插值数量
protocol = {
    'umeeg101', '.vhdr', 0;
    'umeeg103', '.vhdr', 0;
    };

for i = 1:size(protocol, 1)

    % 重新加载数据
    EEG = pop_loadset('filename', [protocol{i, 1} '_epoched.set'], ...
        'filepath', '.');

    % 重新参考，留空的[]是平均重参考，要么你自己填写参考电极
    EEG = pop_reref(EEG, [], 'exclude', [33, 34]);

    % 第一次删坏段
    % 首先找到达到阈值的
    EEG = pop_eegthresh(EEG, 1, ...
        [1:34], ... % 目标通道
        -200, 200, ... % 电压阈值
        EEG.xmin, EEG.xmax, ... % 作用时域
        0, 0);
    bad_epo = find(EEG.reject.rejthresh == 1); % 这个列表里储存marked epochs
    EEG = pop_rejepoch(EEG, bad_epo);

    if 0
    % ica跑起来
    % 首先基线先暂时改一下
    EEG = pop_rmbase(EEG, [EEG.xmin, EEG.xmax]);

    % 根据有无坏道处理不同ica
    if protocol{i, 3} == 0
        EEG = pop_runica(EEG, 'icatype', 'runica', 'extended', 1);
    else
        EEG = pop_runica(EEG, 'icatype', 'runica', 'extended', 1, ...
            'pca', EEG.nbchan - protocol{i, 3});
    end
    end


    % 再保存一下
    pop_saveset(EEG, ...
        ['./' protocol{i, 1} '_ranica.set'])
end


%%
% 删成分，也必须手动，虽然可以依赖ICLabel，然后还用记下来吗？


%%
% 然后最后清一遍的坏段可以再次自动化
% 不过阈值应该怎么找嘞？
% 假设存在三个阈值对应删除率为5，10，33趴
% 那我们的目标就是找到这仨阈值的均值然后存起来
% 这个循环主要找相对阈值，存到protocol列表的新增列好了
for i = 1:size(protocol, 1)

    % 首先读取数据和中心恢复正常基线
    % 不过到时候所读取的文件可能不一样哦
    EEG = pop_loadset('filename', [protocol{i, 1} '_ranica.set'], ...
        'filepath', '.');
    EEG = pop_rmbase(EEG, [EEG.xmin, 0]);


    % 试试找到合理阈值？
    list = {};
    for j = 1:1:40
        thresh = j * 5;
        EEG_temp = pop_eegthresh(EEG, 1, ...
            [], ...
            -thresh, thresh, ...
            EEG.xmin, EEG.xmax, ...
            0, 0);
        list{j, 1} = j;
        list{j, 2} = thresh;
        list{j, 3} = sum(EEG_temp.reject.rejthresh)/length(EEG_temp.reject.rejthresh);
    end


    % 这时候我们手里就有了当前循环被试的阈值-拒绝表格，即list变量
    rej_percent = cell2mat(list(:, 3));
    rej_thresh = cell2mat(list(:, 2));
    
    % 然后这样能够获得最接近那仨删除率对应的索引位置
    [~, id_5] = min(abs(rej_percent - 0.05));
    [~, id_10] = min(abs(rej_percent - 0.1));
    [~, id_33] = min(abs(rej_percent - 0.33));

    % 接着算出来那仨最接近删除率的阈值
    % 不过要进行一步避免极端值的操作
    if rej_thresh(id_5) > 75, rej_thresh(id_5) = 75; end
    if rej_thresh(id_33) < 25, rej_thresh(id_33) = 25; end

    % 最后记录
    protocol{i, 4} = mean(rej_thresh([id_5, id_10, id_33]));
end


%%
% 但是最后最后一步，必须看一眼预处理完成后的数据以确保真的没事了
% 然后终于到了最后一步，所幸最难的部分已经完成了
for i = 1:size(protocol, 1)

    % 读取数据
    EEG = pop_loadset('filename', [protocol{i, 1} '_runica.com'], ...
        'filepath', '.');

    % 极端值删除
    EEG = pop_eegthresh(EEG, 1, ...
        [], ... % 目标通道，具体需要改，下同
        -protocol{i, 4}, ...  % 阈值
        protocol{i, 4}, ...  % 阈值
        EEG.xmin, EEG.xmax, ...  % 作用时域
        0, 0); % 蛋蛋
    bad_epo = find(EEG.reject.rejthresh == 1);
    EEG = pop_rejepoch(EEG, bad_epo);

    % 然后是异常趋势
    EEG = pop_rejtrend(EEG, 1, ...
        [1:32], ...
        500, 50, 0.3, 2, 0, 0);
    extreme_epo = find(EEG.reject.rejtrend == 1);
    EEG = pop_rejepoch(EEG, bad_epo);

    % 异常分布和啥来着不知道
    EEG = pop_jointprob(EEG, 1, ...
    [1:32], ...
    5, 5, 0, 0, 0, [], 0);
    trend_epo = find(EEG.reject.rejjp == 1);
    EEG = pop_rejepoch(EEG, trend_epo);

    EEG = pop_rejkurt(EEG, 1, ...
    [1:32], ...
    5, 5, 0, 0, 0, [], 0);
    kurt_epo = find(EEG.reject.rejkurt == 1);
    EEG = pop_rejepoch(EEG, kurt_epo);


    %最后保存，预处理完成
    pop_saveset(EEG, ...
    ['./' protocol{i, 1} '_preprocessed.set'])
end
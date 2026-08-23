% 初始化
clc; clear all;

% 设置路径
cd('/Users/cheng/Desktop/EEG_study/data_for_study/self_study/batch_single_analysis');



%%
file_list = {
    'umeeg103', '.set';
    'umeeg101', '.set'};
conditions = {
    '201', '202', '203';
    'relevant', 'irrelevant', 'odd'};

% 额外练习1无非也就是嵌套循环，给来自每个被试的数据分epoch以后
% 修改文件头，然后改名存储
for i = 1:size(file_list, 1)

    % 加载文件
    % 但是注意一下，这一步即需要.set也需要.fdt文件
    EEG = pop_loadset('filename', ...
        [file_list{i, 1}, '_10_Pruned_with_ICA', file_list{i, 2}], ...
        'filepath', '.');


    for j = 1:size(conditions, 2)

        % 对每个文件进行condition条件的分类和数据提取
        cEEG = pop_selectevent(EEG, 'latency','-1<=1', ...
            'type', conditions{1, j}, ...
            'deleteevents', 'off', ...
            'deleteepochs', 'on', ...
            'invertepochs', 'off');

        % 提取出来以后修改文件头
        cEEG = pop_editset(cEEG, ...
            'setname', [file_list{i, 1} '_' conditions{1, j}], ...
            'subject', file_list{i, 1}, ...
            'condition', conditions{2, j});

        %保存文件
        pop_saveset(cEEG, [file_list{i, 1} '_' conditions{1, j} file_list{i, 2}]);
    end
end


%%
% 其实还有一个对另一个条件的个体历遍处理
% 就是先选出202 和 201的epochs
% 然后在进一步选择呈现的照片类型
% 然后在分relevant和irrelevant
% 最后editset修改相关信息，比如group参数标注照片类型，再保存数据
% 不过我懒，今天没有动力，效率也不高，直接进入下一章算了
% 唉算了还是搞了把就当练习控制语句了

file_list = {
    'umeeg103', '.set';
    'umeeg101', '.set';
    'umeeg107', '.set'};
conditions = {
    '201', '202', '203';
    'relevant', 'irrelevant', 'odd'};
self = {'self', 'other'};

for i = 1:size(file_list, 1)

    % 加载数据
    EEG = pop_loadset('filename', ...
        [file_list{i, 1}, '_10_Pruned_with_ICA', file_list{i, 2}], ...
        'filepath', '.');

    % 先去除无关条件，就是动物的那个203
    EEG = pop_selectevent(EEG, 'latency','-1<=1', ...
        'type', {'201', '202'}, ...
        'deleteevents', 'off', ...
        'deleteepochs', 'on', ...
        'invertepochs', 'off');

    % 然后开始分类我他条件
    for j = 1:length(self)

        % 不同条件那肯定得进行不同的删选
        % 然后自我照片的marker是1
        if j == 1

                % 然后这里的type之所以是俩是因为
                % Biosemi的marker有时候会在数字前面加上"condition"
                % 然后这里就变成了1 或 condition 1，下同
            cEEG = pop_selectevent(EEG, 'latency','-200<=0', ...
                'type', {'1', 'condition 1'}, ...
                'deleteevents', 'off', ...
                'deleteepochs', 'on', ...
                'invertepochs', 'off');
        else
            cEEG = pop_selectevent(EEG, 'latency','-200<=0', ...
                'type', {'1', 'condition 1'}, ...
                'deleteevents', 'off', ...
                'deleteepochs', 'on', ...
                'invertepochs', 'on');
        end


        % 然后进一步把相关不相关的条件给选出来
        % 然后这一步有个try catch语句可以留意一下
        % 这个语句就是加入报错就执行备用方案
        % 因为自我*相关的各个条件的trial不一定够，
        % 这一步分epoch可能就中间不知道哪里报错
        % 然后用try catch语句执行，报错返回一个信息然后执行下一个文件

        for k = 1:2
            % 因为只要分类201 202，所以这里就1:2


            try
                ccEEG = pop_selectevent(cEEG, 'latency','-1<=1', ...
                    'type', conditions{1, k}, ...
                    'deleteevents', 'off', ...
                    'deleteepochs', 'on', ...
                    'invertepochs', 'off');

                % 修改文件头和保存文件
                ccEEG = pop_editset(cEEG, ...
                    'setname', [file_list{i, 1} '_' self{j} '_' conditions{1, k}], ...
                    'subject', file_list{i, 1}, ...
                    'group', self{j}, ...
                    'condition', conditions{2, k});

                pop_saveset(ccEEG, ...
                    [file_list{i, 1} '_' self{j} '_' conditions{1, k} file_list{i, 2}]);

            catch ME
                % 然后是如果报错怎么办
                % 不耽误它跳过然后执行下一个loop
                disp (ME.message)
                disp ('Probably not enough rel_self epochs!');
                fprintf('Error processing file: %s, condition: %s\n', file_list{i, 1}, conditions{1, k});
                
            end
        end
    end
end
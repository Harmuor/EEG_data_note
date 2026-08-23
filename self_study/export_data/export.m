% 初始化
clc; clear all;

% 设置路径
cd('/Users/cheng/Desktop/EEG_study/data_for_study/self_study/export_data');


%%
% 为了能够进行下去教程，不得不将11章的数据全部覆盖
% 但是我不确定我那个插值是否有问题，最后全tm70个通道了
% 不过实际实验谁tm会用那么极端的情况啊，被试通道数都tm不一样



% 用于循环的准备好变量列表
participant = {
    'umeeg101', 'umeeg102', 'umeeg103', 'umeeg104', ...
    'umeeg105', 'umeeg106', 'umeeg107'
    };

conditions = {
    'rel', 'irr', 'odd'; 
    '201', '202', '203'};

channels = {
    'FC1', 'Cz', 'FC2';  % ROI 1
    'CP1', 'Pz', 'CP2'   % ROI 2
    };

path = '/Users/cheng/Desktop/EEG_study/data_for_study/Chapter 11/data';


%%

% 先给这个循环加个计数功能
count = 0; %用来显示当前所在循环数
total = size(participant, 2) * size(conditions, 2) * size(channels, 1) * size(channels, 2);

% 然后这个空列表用来放置数据
% 因为这个表格我们同时有存字符和数值，所以用cell
% 必须初始化cell的尺寸
% 只是 out_data = {}就是一个1*1的空cell，它不会自动拓展
out_data = cell(512 + 1, total);

for cperson = 1:size(participant, 2)
    for ccond = 1:size(conditions, 2)

        % 数据应该从这里加载
        cEEG = pop_loadset( ...
            'filename', ...
            [participant{cperson} '_11_' conditions{1, ccond} '.set'], ...
            'filepath', path);

        for cROI = 1:size(channels, 1)
            for cchan = 1:size(channels, 2)

                % 数据应该在这里提取然后录入list
                % 首先确定当前通道的号码
                chan_num = find(strcmp({cEEG.chanlocs.labels}, ...
                    channels(cROI, cchan)));
                % 然后把该被试这个通道此条件下的电位平均以后提取出来
                temp_data = mean(cEEG.data(chan_num, :, :), 3);


                % 写入单个cell单元格的时候用{}
                out_data{1, count + 2} = [participant{cperson} '_' conditions{1, ccond} '_ROI' num2str(cROI) '_' channels{cROI, cchan}];
                
                % 写入多个单元格的时候（不是512个数值吗）用()
                out_data(2:end, count + 2) = num2cell(temp_data);
                
                % 写个进度条显示
                count = count + 1;
                fprintf('current pregress: %.2f %% \n', 100 * count/total)
            end
        end
    end
end


% 最后加上时间数据
out_data{1, 1} = 'time';
out_data(2:end, 1) = num2cell(cEEG.times);


%%
% 最后导出数据

% 这是导出为txt
writecell(out_data, './erp_data.txt', 'Delimiter', '\t'); % \t是txt制表符

% 这是导出为csv
writecell(out_data, './erp_data.csv', 'Delimiter', ',');
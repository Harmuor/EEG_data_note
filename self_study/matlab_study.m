% 学学matlab

% 洒家觉得主要是不同的数据类型和操作方法
% 然后还有一些简单的命令学会就好了
% 又回到了数据结构的问题


%%
% 像r一样，要先获取和设置一下工作目录
clc  %清空命令行
clear  %清空工作区
clear all  %大清空
close all  %关闭所有窗口
pwd  %获取当前目录
cd '/Users/cheng/Desktop/EEG_study/data_for_study/self_study'  %切换目录
dir %列出当前目录下内容文件


%%
% 然后变量赋值也就是等号
% 变量命名和R大差不差
a = 1;
b = 'b';
c = 1.1;

% 然后查看变量类型
class(a)


%%
% 然后是tm的数组array
% 它这个既可以用空格分隔也可以用逗号
e = [1 2 3];
f = [1, 2, 3];

e == f;

% 然后它生成数组不用专门的函数
a = [1:10];  %默认步长为1
b = [1:2:10];  %中间的值为步长
c = [10:-1:1];  %步长也可以为负数

% 既然是matlab，那么肯定就是有矩阵的转置
b = a';


%%
% 字符串数组就有点怪怪的好像
% 它实际上把俩字符和合并了
% 自动实现了stringr::str_c(a, b, sep = '')
g = ['fd' 'df'];
g;

% 用逗号也tm一样
g = ['df', 'fd'];
g;


%%
% 二维数组，不就是矩阵吗
% ;表示换行
a = [
    1, 2, 3;
    4, 5, 6]


a' %同样可以使用转置
length(a)  %length和r里面作用差不多，都是返回列数
size(a)  %这个是返回行数和列数
size(a, 1)  %只返回行数
size(a, 2)  %只返回列数，等价length


% 然后就是这个有病的索引
% tm用()而不是[]真tm神经病
a = [
    1, 2, 3;
    4, 5, 6];

a(2, 2)  %可以单个值索引
a(2, 2:3)  %多个值如果连着用:
a(:, 2)  %用:代表所有行/列
a(1, 2:-1:3)  %步长也可以用在索引里
a(end, end)  %end竟然还能这样用


% 它这个索引出来的结果也可以用于变量赋值
b = a(2, 3:-2:1)


% 另外matlab是按列向量索引的
% 比如这里就是返回425，而不是234
a(2:4)


% 除此之外，矩阵变量也可以用于创建新矩阵
b = [a; 7:9]


%%
clear

% 多维数组
% 通过索引创建
a(3, 3, 5) = 12  %使用单个值创建
clear a;
a(2, 3, :) = [1, 2, 3]  %由低维数组创建
clear a
a(:, 2, :, 5) = [3 4 5; 6 7 9; 4 5 6]

%%
% 胞元 cell，克服了数组无法正常储存多个不同类型值的问题
% 这里就像r里的向量和list了
a = {'this', 1}

% 这玩意索引方式和数组一样
a = {1, 2, 3; 4, 5, 6}
a{2, 3:-1:2}


%%
% 结构体 struct
% 《海 纳 百 川》

EEG.name = 'subname101' %创建起来感觉有点像对象
EEG.data = [1 2 3; 4 5 6; 7 8 9]
EEG.Trial.marker = {'201', '202', '203'} %竟然能够接着套，感觉就是r里的list


%%
% 运算
% 四则运算不用说了

% 数组运算，其实就是矩阵运算啦
a = [1, 2, 3];
b = [4, 5, 6];

a + b
a' * b %矩阵乘法
a .* b %点乘


% 逻辑运算跟r差不多，唯一有个不一样的就是不等于号
% 然后结果里面1是T，0是F
2 ~= 2.5  %就是r里面的!=


%%
% 常用命令


% 格式转换命令
% 还是r里面的as.xxx比较方便啊
a = 2;
a = num2str(a);  %数字转字符
a = str2double;  %字符转数字

a = {2 2 2; 3 3 3};
a = cell2mat(a);  %胞元转数组

% 查询变量类型
class(a)

% 然后matlab里面的变量拼接要比r里cat(paste0())直观一丢丢
a = 101;
['umeeg', num2str(a), '_raw.set']  %这个num2str是必要的，不然就乱
['umeeg', a, '_raw.set']


% 然后length还有size就不重复说了，前面有


% 然后find和r里的which差不多
a = [1 2 3 4 5 6];
find(a == 2 | a < 4)

% 但是matlab没有which.min和which.max
% 所以实现起来不一样
[~, id_min] = min(a)
[~, id_max] = max(a)


%%
% 求均值，这里得接触多维数组相关操作了
a(2, :, :) = [1 2 3; 2 3 4]

mean(a, 1)  %average by row，习惯上又好像是按列操作
mean(a, 2)  %average by column，习惯上又好像是按行操作
mean(a, 3)  %把第三维度压缩为1个


clear a
a(:, 2, :, 5) = [3 4 5; 6 7 9; 4 5 6]  %加入是通道*时间*试次*被试

mean(a, 1)  %每个被试每个试次每个时间的通道平均
mean(a, 2)  %每个被试每个试次每个通道的时间点平均
mean(a, 3)  %每个被试在所有试次上的平均ERP喽
mean(a, 4)  %每个试次在所有被试上的平均

% 顺便说一下squeeze()可以用于删掉掉无用维度
% 感觉就是把本来就被mean()压缩的维度的冗余给直接删掉
size(mean(a, 3))
size(squeeze(mean(a, 3)))


% 提取umeeg101第2个通道第300ms的所有事件的平均电位
% 通道*时间点*试次
time = find(abs(EEG.times - 300) < 1, 1);
answer = mean(EEG.data(2, time, :), 3);

% 以上是我的解法，以下为参考解
time = find(abs(EEG.times - 300) < 1, 1);
avg_EEG = mean(EEG.data, 3);
answer = avg_EEG(2, time);


%%
% 函数

% 以下不能通过命令行创建函数，必须tm得另存一个新脚本
% 然后工作目录还得和函数脚本一致才能tm调用
function [output1, output2] = my_function(input1, input2)
% 此处应为此函数摘要
% 此处说明

output1 = input1 * input2;
output2 = input1^2 + input2^2;

end


%%
% for loop和if也不说了
% 就是if 0能跳过，if 1就是不跳了
% 0和1其实就是False和True

% 然后for就是需要 i = 某个数组
% 比如自动命名的loop
a = {};
for i = 1:50
    if i < 10
        a{i} = ['subject0' num2str(i)];
    else
        a{i} = ['subject' num2str(i)];
    end
end


%%
% 画图，tmd为什么每次学画图都tm难死
% 老子也只是为了适应matlibplot才学这个


% 首先生成一个画布
figure;

% 然后定义x y，最后画图
% 感觉怎么那么像baseR都画图
x = 0:0.05:20;
y = sin(x);
plot(x, y)


% 然后图片都美学属性按理说也可以定义的
figure;
x = 0:0.5:20;
y = 4 * x + 5 * x.^2 + 7;  %逐元素平方必须用.^，不然就是对整个x矩阵进行平方
plot(x, y, ...
    'k', ...  %k是颜色为黑色
    'linewidth', 4);  %这里还是那个参数值对儿


% 然后进一步完善这个图片
figure;
axis([4, 18, ...  %x轴上下限
    -0.7, 0.7]);  %y轴上下限

x = 0:0.5:20;
y = 4 * x + 5 * x.^2 + 7;  %逐元素平方必须用.^，不然就是对整个x矩阵进行平方
plot(x, y, ...
    'b', ...  %b是颜色为蓝色
    'linewidth', 4);  %这里还是那个参数值对儿

title('my plot');
xlabel('time');
ylabel('value');


% 画一画EEG的平均电位，第二个通道的每个试次的电位
% 先用eeglab导入一个练一练
figure;
x = EEG.times;
y = mean(EEG.data(2, :, :), 3);
plot(x, y, 'b', 'LineWidth', 4);
title('ERP, channel 2');
xlabel('time');
ylabel('potential');


% 加入同样一幅图画俩试次
figure;
x = EEG.times;
y_1 = mean(EEG.data(1, :, :), 3);
y_2 = mean(EEG.data(2, :, :), 3);
plot(x, y_1, 'r', 'LineWidth', 4);
hold on
plot(x, y_2, 'b', 'LineWidth', 4);
hold off


% 使用循环画第5到第8通道的平均电位
y = [];
figure;
for i = 5:8
    x = EEG.times;
    y(:, i - 4) = mean(EEG.data(i, :, :), 3);
end

plot(x, y, 'LineWidth', 4);  %我靠它竟然能够直接用数组作图而不用在for里逐个提取
title('EEG channel 5 - 8');
xlabel('time');
ylabel('potential');


% 其实教程的理想是这样的，不过其实我觉得我的那个版本更优化
figure;
for i = 5:8
    x = EEG.times;
    y = mean(EEG.data(i, :, :), 3);
    plot(x, y, 'LineWidth', 4)
    hold on
end

hold off


% 除此之外还有功能连接矩阵
% 在时频分析的时候有用]

% 先准备准备变量
a = rand(32, 32);
b = (a + a')/2;

for i = 1:size(b, 1)
    b(i, i) = 1
end

figure;
imagesc(b);  %就是这个玩意，但是如果有数据在r里我应该能画更好看，就是那个相关矩阵换皮呗
colorbar();  %旁边加一个图例


% 然后就是subplot，就是几个图拼在一起的玩意
subplot(2, 2, 1);  %前俩是布局，最后一个是当前目标

% 具体用法
subplot(2, 2, 1);
x = EEG.times;
y = mean(EEG.data(1, :, :), 3);
plot(x, y, 'r', 'LineWidth', 4);

subplot(2, 2, 4);
x = EEG.times;
y = mean(EEG.data(9, :, :), 3);
plot(x, y, 'r', 'LineWidth', 4);
# 直接生成伪随机的刺激呈现list
getwd()
setwd('/Users/cheng/Desktop/EEG_study/eprime-like/list')

library(tidyverse)
library(readxl)

# 这个excell文件是本来就有的，问题是要呈现随机化，历遍
# 同时同一张图片我不期望重复出现
RSVPList <- read_excel('RSVPList.xlsx')

# 首先写一个判定函数
valid <- function(x) {
  
  # 相邻刺激一样的判定
  if(any(x[-1] == x[-length(x)])) {
    return(FALSE)
  }
  
  # 俩怪球挨太近的判定
  oddball_pos_1 <- which(x == './img/101.jpg')
  oddball_pos_2 <- which(x == './img/102.jpg')
  n = abs(oddball_pos_2 - oddball_pos_1)
  if(n <= 30) {
    return(FALSE)
  }
  
  # 如果都没有异常返回true
  return(TRUE)
}



# 用repeat循环，满足条件后退出循环
repeat {
  # 首先随机化
  sam <- sample_n(RSVPList, 62)
  # 然后只有满足no-repeat才能停止随机化抽样
  if (valid(sam) == TRUE) {
    sam
    break
  }
}

# 保存文件，不知道为什么write_csv不行，但是write_csv2可以。
# 然后write_csv又莫名其妙的可以了
write_csv(sam, 'RSVPList.csv')

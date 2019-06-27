rm(list=ls())
library(openxlsx)
t.origin<-read.xlsx("E:/OneDrive/Documents/时间管理/戊戌年/戊戌年秋/0930try.xlsx",colNames=FALSE)
t.origin$X1

######将同名事件的耗时合并
tab<-table(t.origin$X1) #制作一个频数统计表
name1<-names(tab)       #name1中含有全部名
comm<-match(t.origin[,1],name1)#匹配第一列同名项目
output1<-c()
for (i in 1:length(name1)) {
  output1[i]<-sum(t.origin[which(comm==i),-1],na.rm=TRUE)
}
names(output1)<-name1  #output为每一项目所需时间（单位：min）

######将异名同类事件合并
#总目录
class0<-sum(output1)/60
names(class0)<-'合计'

#一级目录
content1<-c('学习时间','工作时间','娱乐时间','自我管理')

#二级、三级目录
##学习
scontent<-c('核心学习','应试学习','其他学习')
scon.c<-c('论文','统计学习','软件学习','英语')#核心学习
scon.a<-c('上课','作业','驾考')#应试学习
scon.e<-c('组会','新闻','课外书')#其他学习
##工作
wcontent<-c('主要工作','其他工作')
wcon.m<-c('北教项目')
##娱乐时间
econtent<-c('手机非正能量','电脑非正能量','其他娱乐')
##自我管理
mcontent<-c('时间管理','财务管理','健康管理')
mcon.h<-c('运动','就医')

#为目录增加内容
library(stringr)
dir<-ls()[str_count(ls(),'con')==1]
dir0<-gsub('content','time',dir)
dir0<-gsub('con','tm',dir0)

class1<-rep(0,length(content1))
names(class1)<-content1


#最后比较
sum(time1==class0)



#fitbit数据以及日期处理
library("fitbitr")
library("ggplot2")
FITBIT_KEY    <- "22D82M"
FITBIT_SECRET <- "9f44ee13ca6fbf9f4a6eebfe4c4692dd"
Sys.setenv(FITBIT_KEY = "22D82M", FITBIT_SECRET = "9f44ee13ca6fbf9f4a6eebfe4c4692dd")
token <- fitbitr::oauth_token()
asleep<-strptime(fitbit[,1],"%Y年%m月%d日 %p%I:%M")
aweak<-strptime(fitbit[,2],"%Y年%m月%d日 %p%I:%M")
sleeptime<-sum(aweak-asleep)


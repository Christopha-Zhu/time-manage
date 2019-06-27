'''
project: 时间管理 1019try-0119try

author:朱谦
'''
import re
import pandas as pd
import datetime
################################将文本读入python中#####################################
f=open('E:\OneDrive\Documents\时间管理\戊戌年\onenote.txt')
octf = f.read() 
f.close()
################################寻找日期的下标#####################################
sep='[0-9]{1,2}月[0-9]{1,2}日.[周|星期][\u4e00-\u9fa5\u767e\u5343\u96f6]{1,10}'
date=re.findall(sep,octf)

a=[0]*len(date)
for i in range(0,len(date)):
    a[i]=octf.find(date[i])

columns=['日','开始','结束','工作段描述','持续 (小时)','持续 (分钟)','任务','标签','工作段细节','任务详细信息']
t=pd.DataFrame(columns=columns)
k=0
def func(x):
    if x=='':
        y=0
    else:
        y=float(x)
    return y

for i in range(0,len(date)):
    if i<107:
        tmp=octf[a[i]:a[i+1]]
    else:tmp=octf[a[i]:]
    #提取当日日期
    date0=date[i].split(' ')[0]
    tmp1=tmp.split('\n')
    task=[0]*len(tmp1)
    for j in range(0,len(tmp1)):
        task[j]=tmp1[j].split('\t')
        if len(task[j])>1:
            tmp0=map(func,task[j][1:len(task[j])])
            if task[j][0]=='':
                task[j][0]=task[j-1][0]
            t.loc[k]=[date0,'','','',0,sum(tmp0),task[j][0],'','','']
            k+=1

tmp=t['日'].str.contains('^1月[0-9]{1,2}日')
t['日'][tmp]='2019年'+t['日'][tmp]
t['日'][-tmp]='2018年'+t['日'][-tmp]
t['日']=pd.to_datetime(t['日'],format='%Y年%m月%d日')

tmp=t['任务'].str.split(' ')
tmp.value_counts()
pd.value_counts
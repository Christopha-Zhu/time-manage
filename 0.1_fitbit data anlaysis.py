import json
import pandas as pd
import os
import re
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
os.chdir(r'E:\OneDrive\Documents\time-manage\MyFitbitData\user-site-export')
file_list = os.listdir()
re_time=re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}')


################## 心率 ##################

def file_extract(reg='^heart_rate-[0-9]{4}-[0-9]{2}-[0-9]{2}.json$'):
    re_heart_rate=re.compile(reg)
    file_heart_rate=[re_heart_rate.findall(i) for i in file_list]
    file_heart_rate = [i[0] for i in file_heart_rate if len(i)>0]
    return file_heart_rate

file_heart_rate=file_extract()

bpm=list()
for i in file_heart_rate:
    f=open(i, 'r+')
    str_json = f.read()
    f.close()
    data = json.loads(str_json)
    bpm0 = [i['value']['bpm'] for i in data]
    bpm_mean = sum(bpm0)/len(bpm0)
    bpm.append(bpm_mean)

bpm_time=[re_time.findall(i)[0] for i in file_heart_rate]
df_bpm = pd.DataFrame({'bpm_time':bpm_time,'bpm':bpm})
df_bpm.to_csv('E:/OneDrive/Documents/time-manage/bpm数据.csv')
################## 睡眠 ##################

file_sleep = file_extract('^sleep-[0-9]{4}-[0-9]{2}-[0-9]{2}.json$')
   
for i in range(len(file_sleep)):
    f=open(file_sleep[i], 'r+')
    str_json = f.read()
    f.close()
    data = json.loads(str_json)
    sleep0 = pd.DataFrame(data)
    sleep0 = sleep0.drop('levels',axis=1)
    if i == 0 :
        sleep = sleep0
    else:
        sleep = sleep.append(sleep0)

sleep['dateOfSleep'] = pd.to_datetime(sleep['dateOfSleep'], format = '%Y-%m-%d') 
sleep.to_csv('E:/OneDrive/Documents/time-manage/sleep.csv')

sleep_daily_elesum = sleep[['minutesAfterWakeup','minutesAsleep','minutesAwake','minutesToFallAsleep','timeInBed']].groupby(sleep['dateOfSleep']).sum()
coln0 = ['dateOfSleep','efficiency','endTime','startTime','timeInBed']
sleep_daily_ele = pd.DataFrame(columns=coln0)
for tmp in sleep[coln0].groupby(sleep['dateOfSleep']):
    line = [0]*5
    line[0] = tmp[0]
    tmp = tmp[1]

    # timeInBed
    line[4] = sum(tmp['timeInBed'])
    # eff
    line[1] = sum([i*j for i,j in zip(tmp['efficiency'],tmp['timeInBed'])])/line[4]
    # endTime
    line[2] = max(tmp['endTime'])
    # startTime
    line[3] = min(tmp['startTime'])
    new_df = pd.DataFrame(line).T
    new_df.columns = coln0
    sleep_daily_ele = sleep_daily_ele.append(new_df)

sleep_daily_ele.index = sleep_daily_ele['dateOfSleep']
sleep_daily_ele = sleep_daily_ele.drop(columns=['dateOfSleep','timeInBed'])
sleep_daily = pd.concat([sleep_daily_ele,sleep_daily_elesum],axis=1)
sleep_daily.to_csv('E:/OneDrive/Documents/time-manage/sleep_daily.csv')

def time2float(x):
    x = x[11:19].split(':')
    x = [float(i) for i in x]
    x = x[0]+x[1]/60+x[2]/60**2
    if x>12:
        x=x-24
    return x

plt.plot(sleep_daily.index,sleep_daily['startTime'].apply(time2float),color='green' )
plt.plot(sleep_daily.index,sleep_daily['endTime'].apply(time2float),color='blue')
plt.show()

# plt.plot(sleep_daily.index,sleep_daily['timeInBed'],color='blue')
plt.figure(figsize=(15,7.5))
plt.plot(sleep_daily.index,24-sleep_daily['minutesAsleep']/60,color='skyblue')
# plt.plot(wkh_daily['date'],wkh_daily['holetime'],color='green')
plt.show()
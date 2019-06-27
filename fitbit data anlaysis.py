import json
f=open('E:/OneDrive/Documents/时间管理/MyFitbitData/user-site-export/heart_rate-2018-12-24.json', 'r+')
str_json = f.read()
data=json.loads(str_json)
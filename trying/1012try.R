library("tidyverse")
library("rlist")
Sys.setenv(TZ="Asia/Shanghai")
starting <- "20171001"
ending <- "20171003"
article_title <- "Yes Minister"
url <- paste("https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents",
             article_title,
             "daily",
             starting,
             ending,
             sep = "/")
library(httr)
response <-GET(url, user_agent="my@email.com this is a test")
library(jsonlite)
toJSON(fromJSON(content(response, as="text")), pretty = TRUE)
result <- fromJSON(content(response, as="text"))
typeof(result)
library(rlist)
df <- list.stack(list.select(result, timestamp, views))
library(lubridate)
library(stringr)

df$timestamp <- ymd(str_sub(df$timestamp, 1, -3))
#然后我们开始转换，先用str_sub函数（来自于stringr软件包）把日期字符串的后两位抹掉，
#然后用lubridate软件包里面的ymd函数，将原先的字符串转换为标准日期格式。
#修改后的数据，我们存储回df$timestamp。


library('RCurl')
path-c("Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOi
I2UVNMSDciLCJhdWQiOiIyMkQ4Mk0iLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLC
JzY29wZXMiOiJ3aHIgd3BybyB3bnV0IHdzbGUgd3dlaSB3c29jIHdhY3Qgd3NldCB3bG9jIiwiZXhwIj
oxNTcwMTU1Nzg4LCJpYXQiOjE1MzkzMDc0Nzh9.QLKFoRP3BjSbHtcnqXKpt9omrzGOFduMgqYEgixtv
VE",https://api.fitbit.com/1/user/-/profile.json)

AUTH_ANY("Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOi
I2UVNMSDciLCJhdWQiOiIyMkQ4Mk0iLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLC
     JzY29wZXMiOiJ3aHIgd3BybyB3bnV0IHdzbGUgd3dlaSB3c29jIHdhY3Qgd3NldCB3bG9jIiwiZXhwIj
     oxNTcwMTU1Nzg4LCJpYXQiOjE1MzkzMDc0Nzh9.QLKFoRP3BjSbHtcnqXKpt9omrzGOFduMgqYEgixtv
     VE",https://api.fitbit.com/1/user/-/profile.json)


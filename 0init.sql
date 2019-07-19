-- 展示有几个database，并使用time_manage
SHOW DATABASES;
USE time_manage;

-- 建表
-- DROP TABLE sleep ;
-- create table sleep(
-- id int,
-- dateOfSleep datetime default NULL,
-- duration int,
-- efficiency FLOAT,
-- endTime VARCHAR(50),
-- infoCode int,
-- logId int,
-- minutesAfterWakeup int,
-- minutesAsleep float,
-- minutesAwake float,
-- minutesToFallAsleep float,
-- startTime VARCHAR(50),
-- timeInBed float,
-- type VARCHAR(50)
-- );

-- DROP TABLE sleep ;
-- create table bpm(
--     id int,
--     bpm_time DATE,
--     bpm float 
-- );

-- DROP TABLE wkh_daily ;
-- create table wkh_daily(
--     id int,
--     date DATE,
--     starttime DATETIME,
--     endtime DATETIME, 
--     type1 FLOAT,
--     type2 FLOAT,
--     type3 FLOAT,
--     type4 FLOAT,
--     type5 FLOAT,
--     holetime FLOAT
-- );



-- 导入csv数据
-- LOAD DATA LOCAL INFILE 'E:/OneDrive/Documents/time-manage/sleep.csv'
-- INTO TABLE sleep
-- FIELDS TERMINATED BY ','
-- IGNORE 1 LINES
-- ;
-- LOAD DATA LOCAL INFILE 'E:/OneDrive/Documents/time-manage/bpm数据.csv'
-- INTO TABLE bpm
-- FIELDS TERMINATED BY ','
-- IGNORE 1 LINES
-- ;
-- LOAD DATA LOCAL INFILE 'E:/OneDrive/Documents/time-manage/wkh_daily.csv'
-- INTO TABLE wkh_daily
-- FIELDS TERMINATED BY ','
-- IGNORE 1 LINES
-- ;

SELECT * FROM wkh_daily LIMIT 1000;
SELECT dateOfSleep FROM sleep ;
#!/usr/bin/env python
# -*-coding:utf-8-*-
import time
import datetime

print(time.strftime('%y-%m-%d %X',time.localtime()))
print(datetime.datetime.now())





















'''
print(dir(time))
print(type(help(time)))
time.sleep(2)
print(time.time())
print(time.ctime())
print(time.ctime(time.time()))
time_gmtime=time.gmtime(time.time())
print(u'查看struct_time格式的显示年月日时分秒结果：\n',str(time_gmtime.tm_year)+'_'+str(time_gmtime.tm_mon)+'_'
+str(time_gmtime.tm_mday)+' '+str(time_gmtime.tm_hour)+':'+str(time_gmtime.tm_min)+':'+str(time_gmtime.tm_sec))
print(time.gmtime(time.time()))
print('%y-%m-%d',time.localtime())
print('%y-%m-%d',time.localtime(time.time()))

print('%y-%m-%d %x',time.localtime())'''



# -*- coding: utf-8 -*-
__author__ = 'baijieying'
import datetime
import time
#http://epaper.gmw.cn/gmrb/html/2016-05/07/nbs.D110000gmrb_01.htm
#http://epaper.tianjinwe.com/tjrb/tjrb/2016-05/09/node_1.htm
#http://paper.people.com.cn/rmrb/html/2016-05/11/nbs.D110000renmrb_01.htm

def get_gmrb():
	#先获得时间数组格式的日期
	starturls=[]
	for i in range(0,16):
		DayAgo = (datetime.datetime.now() - datetime.timedelta(days = i))
		#转换为时间戳:
		#timeStamp = int(time.mktime(threeDayAgo.timetuple()))
		#转换为其他字符串格式:
		otherStyleTime = DayAgo.strftime("%Y-%m/%d")
		starturls.append('http://epaper.gmw.cn/gmrb/html/'+otherStyleTime+'/nbs.D110000gmrb_01.htm')
	print(starturls)
	
def get_rmrb():
	#先获得时间数组格式的日期
	starturls=[]
	for i in range(0,160):
		DayAgo = (datetime.datetime.now() - datetime.timedelta(days = i))
		#转换为时间戳:
		#timeStamp = int(time.mktime(threeDayAgo.timetuple()))
		#转换为其他字符串格式:
		otherStyleTime = DayAgo.strftime("%Y-%m/%d")
		starturls.append('http://paper.people.com.cn/rmrb/html/'+otherStyleTime+'/nbs.D110000renmrb_01.htm')
	print(starturls)

	
def get_tianjin():
	#先获得时间数组格式的日期
	starturls=[]
	for i in range(0,15):
		DayAgo = (datetime.datetime.now() - datetime.timedelta(days = i))
		#转换为时间戳:
		#timeStamp = int(time.mktime(threeDayAgo.timetuple()))
		#转换为其他字符串格式:
		otherStyleTime = DayAgo.strftime("%Y-%m/%d")
		starturls.append('http://epaper.tianjinwe.com/tjrb/tjrb/'+otherStyleTime+'/node_1.htm')
	print(starturls)
    
def get_jjrb():
	#先获得时间数组格式的日期
	starturls=[]
	for i in range(0,365):
		DayAgo = (datetime.datetime.now() - datetime.timedelta(days = i))
		#转换为时间戳:
		#timeStamp = int(time.mktime(threeDayAgo.timetuple()))
		#转换为其他字符串格式:
		otherStyleTime = DayAgo.strftime("%Y-%m/%d")
		starturls.append('http://paper.ce.cn/jjrb/html/'+otherStyleTime+'/node_1.htm')
	print(starturls)
	
if __name__=='__main__':
	get_jjrb()
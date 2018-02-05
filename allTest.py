#!/usr/bin/env python
#-*-coding:utf-8-*-
#—_author:Administrator
#—_date:2018\1\31 0031

import  unittest
import  os
import  HTMLTestRunner
from imp import reload

import sys
reload(sys)

import  time

def suite():
	'''批量获取测试模块'''
	suite=unittest.defaultTestLoader.discover(
		start_dir=os.path.join(os.path.dirname(__file__),'testcase'),
		pattern='test_*.py',
		top_level_dir=None
	)
	return suite

def getNow():
	'''获取当前时间'''
	return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))

def filePath():
	'''获取测试报告的目录'''
	return os.path.join(os.path.dirname(__file__),'report',getNow()+'testReport.html')

def readFile():
	'''二进制写入'''
	fp=open(filePath(),'wb')
	return fp

def run():
	HTMLTestRunner.HTMLTestRunner(
		stream=readFile(),
		title=u'自动化测试报告',
		description=u''
	).run(suite())


if __name__=='__main__':
	run()
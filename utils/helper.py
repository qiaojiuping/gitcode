#!/usr/bin/env python
#-*-coding:utf-8-*-
#—_author:Administrator
#—_date:2018\1\29 0029

import os
import xml.dom.minidom

class DataHelper(object):
	def base_dir(self,path1,path2):
		'''第一个参数是文件夹，第二个参数指文件'''
		return os.path.join(os.path.dirname(os.path.dirname(__file__)),path1,path2)
	def getXmlData(self,value):
		dom=xml.dom.minidom.parse(self.base_dir('data','system.xml'))
		db=dom.documentElement
		name=db.getElementsByTagName(value)
		nameValue=name[0]
		return nameValue.firstChild.data

	def getXmlUser(self,parent,child):
		dom=xml.dom.minidom.parse(self.base_dir('data','system.xml'))
		db=dom.documentElement
		itemlist=db.getElementsByTagName(parent)
		item=itemlist[0]
		return item.getAttribute(child)
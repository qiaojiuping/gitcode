#!/usr/bin/env python
#-*-coding:utf-8-*-
#—_author:Administrator
#—_date:2018\1\29 0029

from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
import time as t

class WebDriver(object):
	def __init__(self,driver):
		self.driver=driver

	def findElement(self,*loc):
		try:
			return self.driver.find_element(*loc)
		except NoSuchElementException as e:
			print('Error details:%s'%e.args[0])
	def wait(self):
		t.sleep(2)
#!/usr/bin/env python
#-*-coding:utf-8-*-
#—_author:Administrator
#—_date:2018\1\29 0029

import unittest
from page.adduser import *
from page.login import *
from selenium import webdriver

class AddUser(unittest.TestCase,AddUser,Login):
	def setUp(self,value='url'):
		self.driver=webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get(self.getXmlData(value))

	def tearDown(self):
		self.driver.quit()

	def test_addshop(self):
		'''验证添加商户'''
		self.login()
		self.isAddShop()
		self.clickMnnage()
		shopName = self.getShopName()
		self.userdelete()
		self.assertEqual(shopName, u'123456')

	if __name__ == '__main__':
		unittest.main(verbosity=2)
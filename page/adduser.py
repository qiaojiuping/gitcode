#!/usr/bin/env python
#-*-coding:utf-8-*-
#—_author:Administrator
#—_date:2018\1\29 0029


from page.login import *
from selenium.webdriver.common.by import By
from base.base import *
from utils.helper import *
class AddUser(WebDriver,DataHelper):
	u'''创建商户'''
	add_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/a')
	account_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[1]/div/input')
	name_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[2]/div/input')
	password_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[3]/div/input')
	save_loc = (By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[9]/div/button')

	def clickAdd(self):
		self.findElement(*self.add_loc).click()

	def typeaccount(self,account):
		self.findElement(*self.account_loc).send_keys(account)

	def typename(self,name):
		self.findElement(*self.name_loc).send_keys(name)

	def typepassword(self,password):
		self.findElement(*self.password_loc).send_keys(password)

	def clickSave(self):
		self.findElement(*self.save_loc).click()

	u'添加商户'
	def useradd(self, parent='class', account='account', name='name', passwords='passwords'):
		self.clickAdd()
		self.typeaccount(self.getXmlUser(parent,account))
		self.typename(self.getXmlUser(parent, name))
		self.typepassword(self.getXmlUser(parent,passwords))
		self.clickSave()

	u'查询'
	so_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/div[2]/input')
	soButton_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/div[3]/button')
	shopName_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div/table/tbody/tr/td[1]/div/a')

	def typeSo(self, name):
		self.wait()
		self.findElement(*self.so_loc).send_keys(name)

	def clickSo(self):
		self.findElement(*self.soButton_loc).click()

	def getShopName(self):
		self.wait()
		return self.findElement(*self.shopName_loc).text


	def so(self, name='123456'):
		self.typeSo(name)
		self.clickSo()

	'''删除商户'''
	clickdelete_loc = (By.XPATH, ".//*[@id='app']/div/div[1]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/div/i")
	choosedelete_loc = (By.XPATH, ".//*[@id='app']/div/div[1]/div[2]/div[2]/div/table/tbody/tr[1]/td[5]/div/ul/li[2]")
	ensuredelete_loc = (By.XPATH, "html/body/div[5]/div[2]/div/div/div/div/div[2]/button[1]")

	def deleteclick(self):
		self.findElement(*self.clickdelete_loc).click()

	def deletechoose(self):
		self.findElement(*self.choosedelete_loc).click()

	def deleteensure(self):
		self.findElement(*self.ensuredelete_loc).click()

	def userdelete(self):
		self.refresh()
		self.deleteclick()
		self.deletechoose()
		self.deleteensure()


	u'商户管理'
	manage_loc = (By.LINK_TEXT, '商户管理')

	def clickMnnage(self):
		self.wait()
		self.findElement(*self.manage_loc).click()

	def isAddShop(self):
		try:
			self.so()
			assert self.getShopName() in u'123456'
			self.userdelete()
		except:
			self.useradd()
		else:
			self.useradd()
		finally:
			pass




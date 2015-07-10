#! /usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import cookielib
from selenium import webdriver 
import codecs
import re
import csv
import sys 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote import webelement
import time
import threading as thread 
reload(sys)
sys.setdefaultencoding('utf-8')
arealist=[330100,330183,330182,330109,330122,330108,330110,330185,330101,
330102,330104,330127,330103,330105,330106]
prefix ='http://218.108.6.116:8080/zxjc/datashow_getdatashowhtml?'
ptype=[1,2]
ttype=['day','hour']
filename='/home/sunying/crawler/hzaqi/monthout/month1.txt'

class Geturl(object):

	def __init__(self,url):
		self.url=url

	def getHtml(self,driver):
		self.driver = webdriver.Firefox()
		self.driver.get(self.url)
		self.soup=self.driver
		return self.soup
	def getTag(self,soup):
		self.tag= self.soup.find_element_by_xpath("/html/body/form/table/tbody/tr/td/div/div/div[2]/table/tbody[2]")
		return self.tag
	def compile(self,tag):
		self.res=re.compile(r'<td class=\S+>(\S+)</td><td class=\S+>(\S+)</td><td class=\S+>(\S+)</td><td class=\S+>(\S+)</td><td class=\S+>(\S+)</td><td class=\S+>(\S+)</td>' or r'<td class=\S+>(\S+)</td><td class=\S+ title=\S+>(\S+)</td><td class=\S+ colspan=\S+>(-)</td>')
		self.result=self.res.findall(str(self.tag))
		return self.result
	def Judge(self,soup):
		selem=self.soup.find_element_by_xpath("//input[@value='下一页']")
		if not selem.get_attribute("disabled"):
			judge=1
		else  :
			judge=0
		return judge 
	def getnextpage(self,soup):
		self.soup.find_element_by_xpath("//input[@value='下一页']").click()
	def quit(self,driver):
		self.driver.quit()
class Output(object):
	def __init__(self,filename):
		self.filename=filename

	def output1(self,filename):
		f=csv.writer(file(filename, 'ab'))
		f.writerow(result)

	def write2(self,filename):
  		with open(filename,'a') as csvfile:
  			spamwriter = csv.writer(csvfile, dialect='excel')
  			spamwriter.writerow(str(result[i]))
  	def writetxt(self,filename,page):
  		f=open(filename,'a')
  		f.write(page)
  	def writetitle(self,filename):
  		f=open(filename,'a')
  		return f
class Nextu(object):

	def __init__(self,urlperfix,p):
		
		self.p = p
		self.urlperfix=urlperfix

	def geturl(self,urlperfix,p):
		self.url ='%sdestiny_page=%s'%(self.urlperfix,self.p)
		return self.url
ptype=2	
ttype="hour"
m=1
i=0
while i<len(arealist):
	
	d=1	
	while d<=31:
		h=0
		while h<=23:
			if h<10:
				url='%swrlx=%s&xzqy=%s&x=41&y=11&sjlx=%s&kssj=2012-%d-%d%%2C%s'%(prefix,ptype,arealist[i],ttype,m,d,'0'+str(h))
			else:
				url='%swrlx=%s&xzqy=%s&x=41&y=11&sjlx=%s&kssj=2012-%d-%d%%2C%s'%(prefix,ptype,arealist[i],ttype,m,d,h) 
			print url
			getpage=Geturl(url)
			output=Output(filename)
			html=getpage.getHtml(url)
			tag=getpage.getTag(html)  
			print tag.text
			# result=getpage.compile(tag)
			# print result
			output.writetitle(filename).write("\n"+'废气-时均值(2012年%d月%d日%s时)'%(m,d,h)+"\n")
			output.writetxt(filename,tag.text)
			judge=1
			while judge:
				getpage.getnextpage(html)
				tag2=html.find_element_by_xpath("/html/body/form/table/tbody/tr/td/div/div/div[2]/table/tbody[2]")
				output.writetxt(filename,tag2.text)
				print tag2.text
				judge=getpage.Judge(html)
				time.sleep(3)
			getpage.quit(html)
				
			h+=1
		d+=1
	i=i+1 	
		

#! /usr/bin/env python
# -*- coding: utf-8 -*-
#import html5lib
import urllib2
import codecs
import re
import csv
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#url='http://www.tutiempo.net/en/Climate/Hangzhou/584570.htm'
year=2012
city='hangzhou'
class Crawler(object):

    def __init__(self,year,month,city):
        self.prefix = 'http://lishi.tianqi.com'
        self.year = year
        self.month = month
        self.city=city
    def url_back(self):
        self.url = '%s/%s/%04d%02d.html' % (self.prefix, self.city, self.year, self.month)
        return self.url 
        #print self.url

    def getHtml(self,url):
        self.page = urllib2.urlopen(self.url)
        self.html = self.page.read()
        self.soup=BeautifulSoup(self.html)
        self.page.close()
        return self.soup

month=1
while month<=12:            
    crawler= Crawler(year,month,city)
    #print crawler.url_back()
    csoup=crawler.getHtml(crawler.url_back())
    csoup=str(csoup)
    soup = BeautifulSoup(csoup)
    #soup= soup.prettify() 
    csoup=soup.find_all("ul",{ "class":"tqtongji2" })
    #print soup

    res=re.compile(r'<td><strong>(\d|\d{2})</strong></td>'+r'<td>(-?\d+\.\d|-?\d{2}|-|\d|-?\d|-?\d+\.\d{2}|-?\d+\.\d{2})</td>'*10)
    result=res.findall(str(csoup))
    with open('/home/sky/local/hz-datasets/hzm-cell-map/hzcrawlerdata/hzwind.csv','a') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        spamwriter.writerow(['%4d-%02d'%(2012,month)])
        spamwriter.writerow(['date','maximun temperature','minimun temperature','weather','wind_direction','wind_power'])        
        i=0
        while i < len(result):
                result[i]=list(result[i])
                spamwriter.writerow(result[i])
                print result[i]
                i+=1
    print month
    month=month+1

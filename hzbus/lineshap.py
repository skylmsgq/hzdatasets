#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from xml.dom import  minidom 
import csv
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import os
#f=csv.writer(file('/home/sunying/hello-jane/weathercrawler/hzbus/try.csv', 'w'))
#f.writerow(['name','x','y','uid','fRoadName','fAroundMarks'])     
i=1
while i<=276:
   
    f=open('/home/sunying/hzbus/raw/line%s.txt'%str(i),'r')
    page = f.read()
    f.close 
    #print 'line%s.txt'%str(i)
    if len(page)!=0:
        xf=open('/home/sunying/crawler/hzbus/line/line%s.xml'%str(i),'w')
        xf.write(str(page))
        xf.close()
        #print 'line%s.xml'%str(i)
        doc = minidom.parse('/home/sunying/crawler/hzbus/line/line%s.xml'%str(i))  
        root = doc.documentElement 
        node = root.getAttribute("name")
        f=open('/home/sunying/hzbus/lineshap.txt','a')
        f.write('\n'+str(node)+";",)
        f.write(root.getAttribute("uid")+";",)
        f.write(root.getAttribute("shape"))
        print shape
    else:
        pass	
    i+=1    

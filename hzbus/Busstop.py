#! /usr/bin/env python
# -*- coding: utf-8 -*-
from xml.dom import  minidom 
import csv
import sys
import Cookie
reload(sys)
sys.setdefaultencoding( "utf-8" )
import os
    
def addline(filename):
    
    f=csv.writer(file(filename, 'ab'),delimiter=';', quoting=csv.QUOTE_MINIMAL)
    f.writerow([uid,name,x,y,fRoadName,fAroundMarks,line])
def addline2(filename):
    f=csv.writer(file(filename, 'ab'))
    f.writerow([name2,linetype])

ls=[] 
ss=[]

#with open('/home/sunying/hello-jane/weathercrawler/hzbus/tryaa.csv','ab') as csvfile:
        #spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    spamwriter = csv.writer(csvfile, dialect='excel') 
#    spamwriter.writerow(['name','x','y','uid','fRoadName','fAroundMarks'])
i=1
while i<=276:

    f=open('/home/sunying/crawler/hzbus/raw/line%s.txt'%str(i),'r')
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

        for n in nodes: 
            uid= n.getAttribute("uid")
            name= n.getAttribute("name")
            x= n.getAttribute("x")
            y= n.getAttribute("y")
            fRoadName= n.getAttribute("fRoadName")
            fAroundMarks= n.getAttribute("fAroundMarks")

            if uid not in ls:
                ls.append(uid)
		nodes2=n.getElementsByTagName("LineName")             
                line='' 
                for n in nodes2:
                    linename=n.getAttribute("uid")
                    line=line+str(linename)
                    linetype=n.getAttribute("type")
                    line=line+","+str(linetype)+","
                    #ss.append(linetype)
                #ss = ss.encode( "UTF-8" )
                addline(r'/home/sunying/crawler/hzbus/Stop.csv')
                print line
                
    else:
        pass
    i+=1   
#print ls
print len(ls) 

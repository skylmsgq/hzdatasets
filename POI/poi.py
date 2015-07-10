# -*- coding: UTF-8 -*-

import json
import urllib2
import pymongo
import random
import time

connection = pymongo.Connection("localhost", 27017)
db_hangzhou = connection['hangzhou']
cnt = 0
# 百度分类
tags = ["美食","宾馆","购物","汽车服务","生活服务","结婚","丽人","金融","休闲娱乐","运动健身","医疗","旅游景点","教育","培训机构","交通设施","房地产","自然地物","行政区划","政府机构","公司企业","门址","道路","交通线"]
# 百度KEYS
apikey = ""
# 记录文件
file = open("count"+str(cnt)+".txt","w")
lng_min, lat_min, lng_gap, lat_gap = 120.0, 30.0, 0.005, 0.005
# for tag in tags:
tag = tags[cnt]
for i in xrange(100):
	for j in xrange(100):
		for x in xrange(28):
			data = ""
			print tag, i, j
			small_lng, small_lat, large_lng, large_lat = lng_min+i*lng_gap, lat_min+j*lat_gap, lng_min+(i+1)*lng_gap, lat_min+(j+1)*lat_gap
			location = str(small_lat)+","+str(small_lng)+","+str(large_lat)+","+str(large_lng)
			url = "http://api.map.baidu.com/place/v2/search?&query="+tag+"&bounds="+location+"&scope=2&output=json&page_size=20&page_num="+str(x)+"&ak="+apikey
			# time.sleep(random.random()*2)
			while True:
				try:
					data = json.load(urllib2.urlopen(url, timeout=3))
					break
				except:
					continue
			if x == 0:
				file.write(str(data["total"])+"\t"+tag+"\t"+str(i)+"\t"+str(j)+"\t"+str(small_lng)+"\t"+str(small_lat)+"\t"+str(large_lng)+"\t"+str(large_lat)+"\n")
			for item in data["results"]:
				db_hangzhou['poi'+str(cnt)].insert(item)
			if len(data["results"]) < 20:
				break			
file.close()

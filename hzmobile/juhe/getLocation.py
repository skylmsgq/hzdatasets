import os
import sys
import urllib2;

#Parameters to change
appkey=sys.argv[1]
serial=int(sys.argv[2])

#Parameters
base_dir=os.path.split( os.path.realpath( sys.argv[0] ) )[0]
main_url="http://v.juhe.cn/cell/get?"
dtype_value="json"
headers={"User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
read_file_name="%s/lac_cid_split/split%d.txt"%(base_dir,serial)
write_file_name="%s/html/html%d.txt"%(base_dir,serial)
mnc_value="0"
lac_value=""
cell_value=""
i=0

fr=open(read_file_name,'r')
fw=open(write_file_name,'w')

for line in fr:
   line=line[:-1]                #erase the last character of line'\n'
   line=line.split('\t')
   lac_value=line[0]             #get lac value
   cell_value=line[1]            #get cell ID value

   url="%skey=%s&dtype=%s&mnc=%s&lac=%s&cell=%s"%(main_url,appkey,dtype_value,mnc_value,lac_value,cell_value)
   req = urllib2.Request(url,headers=headers)
   response= urllib2.urlopen(req)
   html = response.read()
   fw.write(html)
   fw.write("\n")
   i = i+1
   print i
pass

fr.close()
fw.close()



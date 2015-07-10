#Use to deal the Cell Location data
import os
import sys

#Parameters to change
serial=int(sys.argv[1])
print serial

#Parameters
base_dir=os.path.split( os.path.realpath( sys.argv[0] ) )[0]
read_file_name="%s\html\html%d.txt"%(base_dir,serial)
write_file_name="%s\output\out%d.txt"%(base_dir,serial)
i=0

fr=open(read_file_name,'r')
fw=open(write_file_name,'w')

for line in fr:
    if line[15:18]=="200":
       line=line.split("data")
       line=line[1][4:]
       line=line.split("error")
       line=line[0][:-5]
       line=line.split(',')
       for kv in line:
           kv=kv.split(':')
           kv=kv[1][1:][:-1]
           fw.write(kv)
           fw.write("\t")
       pass
       fw.write("\n")
    pass
    i = i+1
    print i
pass

fr.close()
fw.close()
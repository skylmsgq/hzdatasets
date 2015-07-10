#LAC	CELL	Blon	Blat	Glon	Glat	"Location Descriptipn"
# -*- coding: utf-8 -*-  
import os
import sys

#Values
base_dir = os.path.split( os.path.realpath( sys.argv[0] ) )[0]
r_file = "hzwz_data.txt"
w_file = "hz_data.txt"

#Functions
def normalize(rawline,fwrite):
	#deal the raw data of line
	location = rawline.split('\t')[4].decode("utf-8");
	if len(location) != 3:
		if location[4] == "杭".decode("utf-8"):
			fwrite.write(rawline);
		pass
	pass
pass

#Main
fr = open(base_dir + '\\' + r_file,'r')
fw = open(base_dir + '\\' + w_file,'w')

i = 1;
for line in fr:
	normalize(line,fw);
	i = i + 1;
pass

fr.close()
fw.close()



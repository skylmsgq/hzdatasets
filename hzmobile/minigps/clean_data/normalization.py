#LAC	CELL	Blon	Blat	Glon	Glat	"Location Descriptipn"
import os
import sys

#Values
base_dir = os.path.split( os.path.realpath( sys.argv[0] ) )[0]
r_file = "hzm-cell-map.txt"
w_file = "hzwz_data.txt"

#Functions
def normalize(rawline,fwrite):
	#deal the raw data of line
	rawline = rawline.split(";{")
	lc_pair = rawline[0].split(';')
	location = rawline[1].split(',')
	blon = location[1].split(':')[1]
	blat = location[0].split(':')[1]
	l_info = location[3].split(':')[1]
	#write the result to the file
	fwrite.write(lc_pair[0] + '\t' + lc_pair[1] + '\t')
	fwrite.write(blon + '\t' +blat + '\t')
	fwrite.write(l_info)
	fwrite.write('\n')
pass

#Main
fr = open(base_dir + '\\' + r_file,'r')
fw = open(base_dir + '\\' + w_file,'w')

for line in fr:
	normalize(line,fw)
pass

fr.close()
fw.close()



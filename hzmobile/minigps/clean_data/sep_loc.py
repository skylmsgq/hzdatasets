#Blon	Blat
import os
import sys

#Values
base_dir = os.path.split( os.path.realpath( sys.argv[0] ) )[0]
r_file = "hz_data.txt"
w_file = "hz_loc.txt"

#Functions
def normalize(rawline,fwrite):
	#deal the raw data of line
	fwrite.write(rawline.split('\t')[2] + '\t' + rawline.split('\t')[3]);
	fwrite.write('\n');
pass

#Main
fr = open(base_dir + '\\' + r_file,'r')
fw = open(base_dir + '\\' + w_file,'w')

for line in fr:
	normalize(line,fw)
pass

fr.close()
fw.close()



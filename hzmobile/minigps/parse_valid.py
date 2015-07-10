#!/usr/bin/env python
# encoding: utf-8
import sys
from parse_invalid import parseResult

def main():
	if len(sys.argv) < 3:
		print("Usage: thisprogram.py <inputfile> <outputfile>")
		sys.exit()

	ofile = open(sys.argv[2], 'ab') # appended mode
	for line in open(sys.argv[1], 'rb'):
		line = line.strip('\r\n ')
		parts = line.split(';', 2)
		if len(parts) < 3: continue
		lac = parts[0]
		cid = parts[1]
		raw = parts[2]

		status, MSG = parseResult(raw)
		if str(status) == '0':
			ofile.write('%s\n' % line)
	ofile.close()

if __name__ == '__main__':
	main()
#!/usr/bin/env python
# coding: utf-8
# Output invalid pairs
import json
import sys

def parseResult(rawString):
    rdict = json.loads(rawString, encoding='utf-8')
    try:
        status = rdict['status']
        cause = rdict['cause']
        address = rdict['address']
        maptype = rdict['status']
        lon = rdict['lon']
        lat = rdict['lat']
    except KeyError:
        MSG = "ParseJsonError."
        status = None
    else:
        MSG = ';'.join([str(status), str(cause), str(maptype), str(lon), str(lat), address])
    return (status, MSG)


def main():
    if len(sys.argv) < 3:
        print("Usage: thisprogram.py <inputfile> <outputfile>")
        sys.exit()

    ofile = open(sys.argv[2], 'wb')
    for line in open(sys.argv[1], 'rb'):
        line = line.strip('\r\n ')
        parts = line.split(';', 2)
        if len(parts) < 3: continue
        lac = parts[0]
        cid = parts[1]
        raw = parts[2]

        status, MSG = parseResult(raw)
        if str(status) != '0':
            # Write invalid pairs
            #print('%s;%s;%s' % (lac, cid, MSG.encode('utf-8')))
            ofile.write('%s\t%s\n' % (lac, cid))
    ofile.close()

if __name__ == '__main__':
    main()
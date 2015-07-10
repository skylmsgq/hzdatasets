#!/usr/bin/env python
# coding: utf-8
import os
import sys
import urllib2;
import json
import time


def digit2hex(number):
   hexstr = hex(int(number))
   return hexstr.split('x')[1]


def requestMinigps(lac, cid):
   prefix = 'http://minigps.org/as'
   mcc = '1cc'
   mnc = '0'
   lac = lac
   cid = cid
   signal = 'AC'
   p = 1 # plain text
   mt = 1 # baidu latitude
   needaddress = 1 # address string
   URL = "%s?x=%s-%s-%s-%s-%s&p=%d&mt=%d&needaddress=%d" % (prefix, mcc, mnc, lac, cid, signal, p, mt, needaddress)
   #print URL

   headers={
      "User-Agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1",
      "Keep=Alive": "timeout=15, max=999"}
   req = urllib2.Request(URL ,headers=headers)
   response= urllib2.urlopen(req)
   html = response.read()
   return html


def check_path(filename):
   dname = os.path.dirname(filename)
   if not os.path.exists(dname):
      os.makedirs(dname)
   elif os.path.exists(filename):
      os.remove(filename)
   return True


def write2file(line, fname):
   if line[-1] not in ['\r', '\n']:
      line += '\n'
   open(fname, 'ab').write(line)


def main():
   if len(sys.argv) < 2:
      print("Usage: thisprogram.py <inputfile> [job_number]")
      sys.exit()

   try:
      jid = sys.argv[2]
   except KeyError:
      jid = 0

   # Prepare output files
   file_raw = os.path.join(str(jid), 'result-raw.txt')
   file_clean = os.path.join(str(jid), 'result-clean.txt')
   file_problem = os.path.join(str(jid), 'result-problem.txt')
   check_path(file_raw)
   check_path(file_clean)
   check_path(file_problem)

   ifile = open(sys.argv[1], 'r')
   i = 0
   for line in ifile:
      i += 1
      line = line.strip('\r\n ')
      if len(line) == 0: continue
      parts = line.split('\t')
      if len(parts) < 2 : continue
      lac = parts[0]
      cid = parts[1]
      if '' in [lac, cid]: continue # an empty line or invalid lac-cid pair
      print('Worker %s: %d %s %s') % (str(jid), i, lac, cid)

      try:
         rawRes = requestMinigps(digit2hex(lac), digit2hex(cid))
      except urllib2.URLError, e:
         # Record failed pair
         write2file('%s;%s;%s\n' % (lac, cid, e), file_problem)
         continue

      # Write raw results
      write2file('%s;%s;%s\n' % (lac, cid, rawRes), file_raw)
      
      time.sleep(0.5) # be soft to server

   ifile.close()


if __name__ == '__main__' :
   main()

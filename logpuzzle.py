#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
	lis1=[]
	lis2=[]
	match=re.search(r'code.google.com',filename)
	f1=match.group()
	f=open(filename,'r')
	lis=re.findall(r'[\w/.-]+puzzle[\w/.-]+',f.read())	
	for i in lis:
		lis1.append('http://'+f1+i)
	for i in lis1:
		if i not in lis2:
			lis2.append(i)
	c=[]
	for i in lis2:
	     b=re.search(r'\w+.jpg',i)
	     c.append(b.group())
	c.sort()
	lis3=[]
	for i in c:
		for j in lis2:
			match=re.search(i,j)
			if match:
				lis3.append(j)
	print lis3
	f.close()
	return lis3
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  count=0
  if not os.path.exists(dest_dir):
	os.mkdir(dest_dir)
  dest_dir=os.path.abspath(dest_dir)
  index=open(os.path.join(dest_dir,'index.html'),'w')
  index.write('<html><body>\n')
  for i in img_urls:
	print i
	print'///downloading...'
	img='img%d'%count
	urllib.urlretrieve(i,os.path.join(dest_dir,img))
	index.write('<img src="%s">' % (img,))
	count=count+1
  index.write('</body></html>\n')
  index.close()

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
  img_urls=[]
  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()

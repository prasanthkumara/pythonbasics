#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""
def absolute(dirname):
  result = []
  paths = os.listdir(dirname)  # list of paths in that dir
  for fname in paths:
    match = re.search(r'__(\w+)__', fname)
    if match:
      result.append(os.path.abspath(os.path.join(dirname, fname)))
  return result
		
# Write functions and modify main() to call them
def cpy(paths,dirname):
	if not os.path.exists(dirname):
		os.mkdir(dirname)
	for path in paths:
   	 	fname = os.path.basename(path)
    		shutil.copy(path, os.path.join(to_dir, fname))
	
def tzip(path,zfile):
	arg='zip -j '+zfile+' '+' '.join(path)
	print "Command I'm going to do:" + arg
	(status,output)=commands.getstatusoutput(arg)
	if status:
		sys.stderr.write(output)
		sys.exit(1)
	
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  paths=[]
  for dirname in args:
  	paths.extend(absolute(dirname))
  if todir:
	cpy(paths,todir)
  if tozip:
	tzip(paths,tozip)

if __name__=="__main__":
	main()

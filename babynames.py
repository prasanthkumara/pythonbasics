#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename,file1):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  
  
  fil=open(filename,'r')
  txt=fil.read()
  fil.close()
  m=re.search(r'\d+',(re.search('Popularity in \d+[<]',txt)).group())
  fil1=open(file1,'w')
  fil1.write(m.group())
  count=1
  asso={}
  lis=re.findall('<td>\S+</td><td>\S+</td>',txt)
  for i in lis:
    line=re.findall(r'>\w+<',i)
    asso[line[1][1:-1]]=line[0][1:-1]
    asso[line[2][1:-1]]=line[0][1:-1]

  for keys in sorted(asso.keys()):
    fil1.write('\n')
    fil1.write(keys+' ::: '+asso[keys])  
  fil1.close()
  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print 'usage: [--summaryfile] file file name to write'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  if len(args)!=2:
    print 'not specified the file to get the output'
    sys.exit(1)
  extract_names(args[0],args[1])

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()

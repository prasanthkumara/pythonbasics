#!/usr/bin/python -tt
import random
import sys
import re


def mimic_dict(filename):
  fi=open(filename,'r')
  lis=fi.read()
  fi.close()
  tt=lis.split()
  start=' '
  mimic={}
  for i in tt:
  	if start not in mimic:
  		mimic[start]=[i]
  	else:
  		mimic[start].append(i)
  	start=i

  return mimic


def print_mimic(mimic_dict, word):
  for i in range(200):
    print word,
    j = mimic_dict.get(word)         
    if not j:
      j = mimic_dict[' '] 
    word = random.choice(j)


def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, ' ')


if __name__ == '__main__':
  main()

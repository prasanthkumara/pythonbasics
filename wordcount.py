#!/usr/bin/python -tt
import sys
import re
def read_file(filename):
	fileob=open(filename,'r')
	txt=fileob.read()
	fileob.close()
	txt=re.findall(r"\w+",txt)
	asso={}
	for i in txt:
		i.lower()
		if i not in asso:
			asso[i]=1
		else:
			asso[i]=asso[i]+1
	return asso	


def print_words(filename):
	asso={}
	asso=read_file(filename)
	for key in sorted(asso.keys()):
		print key+' '+'::'+' '+str(asso[key])+'\n'
		

def print_top(filename):
	asso={}
	asso=read_file(filename)
	count=1
	for values in sorted(asso.values(),reverse=1):
		if count<=20:
			for j in asso:
				if values == asso[j]:
					print j+' '+'::'+' '+str(values)
					count=count+1
		else:
			sys.exit(1)
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()

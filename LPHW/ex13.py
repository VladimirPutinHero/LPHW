#encoding=utf-8

from sys import argv

script, filename = argv
f = open(filename)
print f.read()
f.close()

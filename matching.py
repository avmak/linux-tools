#!/usr/bin/python
# -*- coding: utf-8 -*-

# The script takes two files and compares the lines of the first file with lines of the second file.
# Then it displays the difference in file diff.txt.
# Usage: ./matching.py files1 files2

import sys

def makelst(infile):
  lst = []
  for line in open(infile):
    lst.append(line)
  return lst

lst1 = makelst(sys.argv[1])
lst2 = makelst(sys.argv[2])

with open('diff.txt', 'w') as d:
  for i in lst1:
    if i not in lst2:
      d.write(i)

print 'Compare performed!'

#!/usr/bin/env python
import sys

filename = sys.argv[1]

inputfile = open(filename)

for i in range(1,1+int(inputfile.read())):
    if   i % 15 == 0: print 'Hop'
    elif i %  5 == 0: print 'Hophop'
    elif i %  3 == 0: print 'Hoppity'

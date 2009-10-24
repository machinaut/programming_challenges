#!/usr/bin/env python
import sys

if len(sys.argv) != 2: print 'usage: ./liarliar <infile>'; exit(-1)

f = open(sys.argv[1])

num_accusers = int(f.readline())

grpA, grpB, nul = set(), set(), set()

for accuser in xrange(num_accusers):
    name, num = f.readline().split()
    liars = set()
    for i in xrange(int(num)): liars.add(f.readline().strip())
    if not(name in grpA or name in grpB):
        if liars <= grpA: grpB.add(name)
        else: grpA.add(name)        

a, b = len(grpA), len(grpB)
print max(a,b), min(a,b)

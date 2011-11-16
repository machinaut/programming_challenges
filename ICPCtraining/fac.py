#!/usr/bin/env python
def fac(n):
  if n == 1: return 1
  return n*fac(n-1)

for i in range(1,14):
  print fac(i)

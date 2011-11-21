#!/usr/bin/env python
def baseN(num,b):
  if num==0:return"0"  
  return baseN(num//b,b).lstrip("0")+"0123456789abcdefghijklmnopqrstuvwxyz"[num%b]

def norm(num):
  l = [int(i) for i in list(num)]
  off = max(l)+1
  l = [i+off for i in l]
  m = 0
  for i in range(len(l)):
    if l[i] < off:
      continue
    l = map(lambda x: m if x ==l[i] else x, l)
    m += 1
  return ''.join([str(i) for i in l])


def numbers(n):
  s = set()
  for i in range(n**n):
    num = baseN(i,n)
    s.add("0"*(n-len(num))+num)
  return s

if __name__ == "__main__":
  import sys
  n = int(sys.argv[1])
  l = [int(i) for i in set([norm(i) for i in numbers(n)])]
  l.sort()
  for i in l: print i


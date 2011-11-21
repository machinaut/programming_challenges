#!/usr/bin/env python
def combosn(n):
  count = 0
  maxs = [0]*n
  state = [0]*n
  while True:
    print state[::-1]
    count += 1
    state[0] += 1
    for i in range(n-1):
      if state[i] > maxs[i+1]+1:
        state[i] = 0
        state[i+1] += 1
      else: 
        maxs[i+1] = max(state[i+1],maxs[i+1])
        break
    if state[n-1] > 0 : break
  print count

def combos6():
  count = 0
  ma = [0,0,0,0]
  for i in range(1):
    for j in range(2):
      ma[0] = max(i,j)
      for k in range(3):
        if k > ma[0]+1: break
        ma[1] = max(k,ma[0])
        for l in range(4):
          if l > ma[1] + 1: break
          ma[2] = max(l,ma[1])
          for m in range(5):
            if m > ma[2] + 1: break
            ma[3] = max(m,ma[1])
            for n in range(6):
              if n > ma[3] + 1: break
              print [i,j,k,l,m,n],ma
              count += 1
  print count

def combos5():
  count = 0
  ma = [0,0,0]
  for i in range(1):
    for j in range(2):
      ma[0] = max(i,j)
      for k in range(3):
        if k > ma[0]+1: break
        ma[1] = max(k,ma[0])
        for l in range(4):
          if l > ma[1] + 1: break
          ma[2] = max(l,ma[1])
          for m in range(5):
            if m > ma[2] + 1: break
            print [i,j,k,l,m],ma
            count += 1
  print count

def combos4(): # correct!
  count = 0
  m = [0,0]
  for i in range(1):
    for j in range(2):
      m[0] = max(i,j)
      for k in range(3):
        if k > m[0]+1: break
        m[1] = max(k,m[0])
        for l in range(4):
          if l > m[1] + 1: break
          print i,j,k,l, m
          count += 1
  print count

def combos3(): # correct!
  count = 0
  m = [0]
  for i in range(1):
    for j in range(2):
      m[0] = max(i,j)
      for k in range(3):
        if k > m[0]+1: break
        print i,j,k
        count += 1
  print count

def combos2(): # correct!
  count = 0
  for i in range(1):
    for j in range(2):
      print i,j
      count += 1
  print count

def combos1(): # correct!
  count = 0
  for i in range(1):
    print i
    count += 1
  print count

if __name__ == "__main__":
  combos6()

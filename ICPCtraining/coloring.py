#!/usr/bin/env python
def combosn(n):
  count = 0
  maxs = [0]*n
  state = [0]*n
  while True:
    print state[::-1]#,maxs[n-2:0:-1]
    count += 1
    state[0] += 1
    for i in range(n-1):
      if state[i] > maxs[i+1]+1:
        state[i] = 0
        state[i+1] += 1
      else: 
        for j in range(i,0,-1):
          maxs[j] = max(state[j],maxs[j+1])
        break
    if state[n-1] > 0 : break
  print count

def combosnk(n,k):
  l = []
  count = 0
  state = [0]*(n-k) + range(k)[::-1]
  maxs = [k-1]*(n-k) + range(k)[::-1]
  while True:
    l.append( state [::-1] )
    count += 1
    state[0] += 1
    for i in range(n-1):
      if state[i] > maxs[i+1]+1 or state[i] > k-1:
        state[i] = 0
        state[i+1] += 1
      else: 
        for j in range(i,0,-1):
          maxs[j] = min(max(state[j],maxs[j+1]),k-1)
        break
    if state[n-1] > 0 : break
  return l

if __name__ == "__main__":
  import sys
  combosn(int(sys.argv[1]))

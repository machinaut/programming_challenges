#!/usr/bin/env python
def colorings(n,k):
  state = range(1,k)[::-1]+[1]*(n-k)=[0]
  maxs = state.copy()
  base = range(k)[::-1]+[0]*(n-k)
  while True:
    yield state
    for i in range(n-1):
      if state[i] > maxs[i+1]+1:
        state[i] = 0
        state[i+1] += 1
      else:
        for j in range(i,0,-1):
          maxs[i] = max(state[j],maxs[j+1])
          if maxs[j] < base[j]:
            maxs[j] = state[j] = base[j]
        break
    if state[n-1] > 0: break

if __name__ == "__main__":
  animosity = []
  names = {}
  next = 0
  for line in f.readlines():
    a,b = line.split()
    if a not in names:
      names[a] = next
      next += 1
    if b not in names:
      names[b] = next
      next += 1
    animosity.append((names[a],names[b]))
  for k in range(1,n+1): # for k colors
    for color in colorings(n,k):
      for pair in animosity:
        a,b = pair
        if color[a] == color[b]: break
      else:
        print k; exit(0)


#!/usr/bin/env python
import sys

def bipartite(ext):
    grpA, grpB = set(), set()
    while ext != []: # will not halt on bad input
        for i, (name, liars) in enumerate(ext):
            if not(name in grpA or name in grpB):
                if liars <= grpA or (grpA == grpB == set()):
                    grpB.add(name)
                    grpA |= liars
                elif liars <= grpB:
                    grpA.add(name)
                    grpB |= liars
                else: # no idea where they go
                    continue
            elif name in grpA:
                grpB |= liars
            else: #name in grpB
                grpA |= liars
            del ext[i]
    return grpA, grpB

if __name__ == "__main__":
    f = open(sys.argv[1])
    num_accusers = int(f.readline())

    ext = []
    for accuser in xrange(num_accusers):
        name, num = f.readline().split()
        liars = set()
        for i in xrange(int(num)):
            liars.add(f.readline().strip())
        ext.append((name,liars))

    grpA, grpB = bipartite(ext)
    a, b = len(grpA), len(grpB)
    print max(a,b), min(a,b)

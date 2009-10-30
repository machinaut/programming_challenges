#!/usr/bin/env python
import sys

def brute(filename):
    input = open(filename) # input file
    bag = int(input.readline().strip()) # max weight we have to drop

    items = [] #(SKUs, weights, costs, ratios), ...
    r = 1 # number of possible combinations of items

    for line in input:
        SKU, weight, cost = line.split()
        max = (bag + int(weight) - 1)/ int(weight) + 1 # max qty of this item
        r *= max # add this item's contribution to possible combinations
        items.append((int(weight), int(cost), max))

    best = None # best cost solution
    for i in xrange(r):
        totalweight = 0
        totalcost = 0
        for weight, cost, max in items:
            qty, i = i % max, i / max
            totalweight += qty * weight
            totalcost += qty * cost
        if totalweight >= bag and (best is None or totalcost < best):
            best = totalcost
    return best

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'usage: ./brute.py <inputfile>'
        exit(1)
    print brute(sys.argv[1])

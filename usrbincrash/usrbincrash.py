#!/usr/bin/env python
import sys

if len(sys.argv) < 2:
	print "Please provide a filename."
	exit(1)

f = open(sys.argv[1])
weight = int(f.readline().strip())

SKUs, weights, costs, ratios = [], [], [], []

for line in f:
    SKU, weight, cost = line.split()
    SKUs.append(SKU)
    weights.append(int(weight))
    costs.append(int(cost))
    ratios.append(float(cost)/weight)



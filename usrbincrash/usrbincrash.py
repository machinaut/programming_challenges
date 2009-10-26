#!/usr/bin/env python
import sys
f = open(sys.argv[1])
weight = int(f.readline().strip())

SKUs, weights, costs, ratios = [], [], [], []

for line in f.readlines():
    SKU, weight, cost = line.split()
    SKUs.append(SKU)
    weights.append(int(weight))
    costs.append(int(cost))
    ratios.append(float(cost)/weight)



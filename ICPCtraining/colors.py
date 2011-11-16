#!/usr/bin/env python
import sys
from pprint import pprint

def next_color(lst_item):
    nxt_lst = []
    if type(lst_item) is list:
        for i,sub in enumerate(lst_item):
            lst_item[i] = map(next_color, sub)
        return lst_item
    else:
        nxt_sub = []
        for i in xrange(lst_item+2):
            nxt_sub.append(i)
        nxt_lst.append(nxt_sub)
        return nxt_lst


if __name__ == "__main__":
    step = [0]
    num_steps = 1
    if len(sys.argv) >= 2:
        num_steps = int(sys.argv[1])

    for i in xrange(num_steps):
        step = map(next_color, step)
    pprint(step)

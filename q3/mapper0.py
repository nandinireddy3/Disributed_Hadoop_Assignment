#!/usr/bin/env python3

import sys

root = 1

for line in sys.stdin.readlines():
    line = line.strip().split()

    node = int(line[0])

    if(node == root):
        print(f"{node}\t0 {' '.join(line[1:])}")
    else:
        print(f"{node}\tinf {' '.join(line[1:])}")

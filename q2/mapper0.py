#!/usr/bin/env python3

import sys

for line in sys.stdin.readlines():
    line = line.strip()
    nodes = line.split()

    # Assuming the input format is "node1 node2" for an edge
    print(f"{nodes[0]}\t{nodes[1]}")
    print(f"{nodes[1]}\t{nodes[0]}")

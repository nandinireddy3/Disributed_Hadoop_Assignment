#!/usr/bin/env python3

import sys

# Initialize an empty dictionary to store adjacency lists
adjacency_dict = {}

for line in sys.stdin:
    line = line.strip()
    node, neighbor = line.split('\t')

    if node not in adjacency_dict:
        adjacency_dict[node] = set()

    adjacency_dict[node].add(neighbor)

# Emit the final adjacency lists
for node, neighbors in sorted(adjacency_dict.items()):
    print(f"{node}\t{' '.join(sorted(neighbors))}")


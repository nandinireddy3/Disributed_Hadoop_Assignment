#!/usr/bin/env python3

import sys

for line in sys.stdin.readlines():
    # Split the input line into vertex and its neighbors
    parts = line.strip().split()
    vertex = int(parts[0])
    neighbors = list(map(int, parts[1:]))
    
    # Emit key-value pairs for each pair of neighbors
    for i in range(len(neighbors)):
        for j in range(i + 1, len(neighbors)):
            print(f"{neighbors[i]} {neighbors[j]}\t{vertex}")

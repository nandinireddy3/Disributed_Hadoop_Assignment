#!/usr/bin/env python3

import sys
from collections import defaultdict

current_key = None
current_values = defaultdict(set)

for line in sys.stdin.readlines():
    # Split the input line into key-value pairs
    key_value, vertex = line.strip().split("\t")
    key = tuple(map(int, key_value.split()))
    
    # Add vertex to the set for the current key
    current_values[key].add(int(vertex))

# Sort and output the results
for key, values in current_values.items():
    if len(values):
        print(f"{key[0]} {key[1]}\t{' '.join(map(str, sorted(values)))}")

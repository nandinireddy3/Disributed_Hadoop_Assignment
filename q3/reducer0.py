#!/usr/bin/env python3

import sys

def emit(key, value):
    print(f"{key}\t{value}")

def isVertex(data):
    return len(data) > 1

def reducer(node_id, data):
    updated_distance = float('inf')
    adjacency_list = []
    
    for value in data:
        val = float(value[0])
        if isVertex(value):
            adjacency_list = value[1:]
        updated_distance = min(updated_distance, val)

    if(updated_distance != float('inf')):
        updated_distance = int(updated_distance)
    emit(node_id ,f"{updated_distance} {' '.join(adjacency_list)}")

if __name__ == "__main__":
    current_node_id = None
    current_data = {}

    for line in sys.stdin.readlines():
        node_info = line.strip().split()
        node_id = node_info[0]
        data = node_info[1:]

        if node_id not in current_data:
            current_data[node_id] = []

        current_data[node_id].append(data)

    for node, in_data in current_data.items():
        reducer(node,in_data)

    

        



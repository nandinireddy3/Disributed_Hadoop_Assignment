#!/usr/bin/env python3

import sys

limit = 10

if __name__ == "__main__":
    current_node_id = None
    current_data = {}

    for line in sys.stdin.readlines():
        node_info = line.strip().split()
        node_id = node_info[0]
        dist = node_info[1]

        if(float(dist) <= limit):
            print(f"{node_id}\t{dist}")


    

        



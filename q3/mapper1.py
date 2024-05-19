#!/usr/bin/env python3

import sys

for lines in sys.stdin.readlines():
    line = lines.strip()
    node_info = line.split()

    node = int(node_info[0])
    node_info = node_info[1:]

    dist = node_info[0]
    adj_list = node_info[1:]

    print(line)

    for m in adj_list:

        d = 'inf'
        if dist != 'inf':
            d = int(dist)+1
        
        print(f"{m}\t{d}")
        # print(m,' ',d)
    

#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heapify, heappush, heappop

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

def prims(n, edges, start):
    # Write your code here
    # heapify all edges by weight in a min heap
    heap = []
    heapify(heap)
    weight = 0
    for v1, v2, w in edges:
        heappush(heap, (w,v1,v2))
    mst_so_far = set()
    mst_so_far.add(start)
    nodes_rem = set(list(range(1,n+1)))
    nodes_rem.remove(start)
    print(nodes_rem)
    m = len(edges)
    while len(nodes_rem) > 0:
        w, v1, v2 = heappop(heap)
        #print("w: ", w, " v1: ", v1, " v2: ", v2)
        reinsert = []
        while (v1 in nodes_rem and v2 in nodes_rem) or (v1 in mst_so_far and v2 in mst_so_far):   
            reinsert.append((w,v1,v2))
            w, v1, v2 = heappop(heap)
            print("w: ", w, " v1: ", v1, " v2: ", v2)
        # v1 and v2 are in separate sets
        for dw, dv1, dv2 in reinsert:
            heappush(heap, (dw,dv1,dv2))
        weight += w
        if v1 in mst_so_far:
            nodes_rem.remove(v2)
            mst_so_far.add(v2)
        else:
            nodes_rem.remove(v1)
            mst_so_far.add(v1)
        #print("w: ", w)
        #print("v1: ", v1, " v2: ", v2)
        #print("nodes rem: ", nodes_rem)
    return weight
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()

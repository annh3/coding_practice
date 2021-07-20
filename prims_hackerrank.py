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
    mst_count = 0
    while mst_count < len(edges):
        w, v1, v2 = heappop(heap)
        

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

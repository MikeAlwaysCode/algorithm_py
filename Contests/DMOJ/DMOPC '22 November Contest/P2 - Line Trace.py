import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    arr = ints()
    s = set(arr)
    if len(s) < n:
        print(-1)
        return
    
    edge = dict()
    for i, a in enumerate(arr, 1):
        if i == a: continue
        if i < a:
            step = -1
        else:
            step = 1
        print(a, "->", i)
        for j in range(a, i, step):
            to = j + step
            # u, v = min(j, to), max(j, to)
            # edge.append((j, to))
            # if j not in edge or 
            edge[(j, to)] = i
            edge[(to, j)] = 0
    
    print(len(edge))
    print(edge)

    # ans = 0

    # print(ans)

# t = int(input())
# for _ in range(t):
solve()
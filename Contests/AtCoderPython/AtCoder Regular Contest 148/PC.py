import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n, q = map(int, input().split())
    child = [0] * (n + 1)
    
    parent = [-1, -1] + ints()  # parent of 1 is -1

    for i in range(2, n + 1):
        child[parent[i]] += 1   # count childs of vertex
    
    for i in range(q):
        _, *v = ints()
        # s = {*v}
        s = set(v)
        # for vertex c:
        # if parent not in s, press c and all its childs once
        # if parent in s, it and its childs will be pressed in its parent's operation,
        #    actually it should not be pressed, so -1
        print(sum((child[c] + (-1 if parent[c] in s else 1) for c in v)))


# t = int(input())
# for _ in range(t):
solve()
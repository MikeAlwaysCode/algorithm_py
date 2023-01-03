import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    arr = ints()
    
    odd = sum([a & 1 for a in arr])
    if odd == 0 or odd == n:
        print(0)
    else:
        print(n - odd)


t = int(input())
for _ in range(t):
    solve()
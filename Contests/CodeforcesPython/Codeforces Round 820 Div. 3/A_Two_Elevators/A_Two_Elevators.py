import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    a, b, c = map(int, input().split())
    
    k1 = a - 1

    k2 = abs(c - b) + c - 1

    print(1 if k1 < k2 else 2 if k1 > k2 else 3)

t = int(input())
for _ in range(t):
    solve()
import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    w, x, y, z = map(int, input().split())

    print(w + (x - y) * z)

t = int(input())
for _ in range(t):
    solve()
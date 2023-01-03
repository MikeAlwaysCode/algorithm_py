import collections
import itertools
import math
import random
import sys
from functools import reduce
from heapq import heapify, heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n, m = map(int, input().split())
    r = g = 0

    if n & 1 and m & 1:
        r, g = min((n + 1) // 2 * m, (m + 1) // 2 * n), max(n // 2 * m, m // 2 * n)
    else:
        r, g = n * m // 2, n * m // 2

    print(r, g)

# t = int(input())
# for _ in range(t):
solve()
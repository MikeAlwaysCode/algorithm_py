import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

MOD = 10 ** 9 + 7

def solve() -> None:
    n, k = map(int, input().split())
    s = str(input())

    if k == n:
        print(2)
    elif k & 1:
        print(pow(2, n, MOD))
    else:
        print(pow(2, n-1, MOD))

t = int(input())
for _ in range(t):
    solve()
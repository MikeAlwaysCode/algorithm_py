import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n, k = map(int, input().split())

    if n % k == 0:
        print(0)
    else:
        print(1)

t = int(input())
for _ in range(t):
    solve()
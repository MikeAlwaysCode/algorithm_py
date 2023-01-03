import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n, m = map(int, input().split())

    if n == 1 or m == 1 or (n & 1 and m & 1):
        print("No")
    else:
        print("Yes")

t = int(input())
for _ in range(t):
    solve()
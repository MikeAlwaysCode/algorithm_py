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

    for i in range(1, n):
        print(i, n)

    k = m - n + 1
    fr = 1
    l = 1
    while k:
        to = fr + l
        if to > n - 1:
            to -= n - 1
        print(fr, to)
        fr += 1
        if fr > n - 1:
            fr = 1
            l += 1
        
        k -= 1

# t = int(input())
# for _ in range(t):
solve()
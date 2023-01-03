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
    s = input().strip()
    if n <= 2:
        print(s)
    else:
        zero = s.count("0")
        print("0" * zero + "1" * (n - zero))

t = int(input())
for _ in range(t):
    solve()
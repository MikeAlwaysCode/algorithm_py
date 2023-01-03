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
    
    mn = (k + 1) * k // 2

    if n >= mn:
        print("Yes")
    else:
        print("No")

t = int(input())
for _ in range(t):
    solve()
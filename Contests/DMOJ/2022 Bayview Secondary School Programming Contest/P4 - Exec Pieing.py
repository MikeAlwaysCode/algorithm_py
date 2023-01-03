import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n, t = map(int, input().split())
    arr = ints()

    cnt = mx = 0
    for i, a in enumerate(arr):
        mx = max(mx, a)
        cnt += a
        if cnt > t + mx:
            print(i - 1)
            return
    
    print(n - 1)

# t = int(input())
# for _ in range(t):
solve()
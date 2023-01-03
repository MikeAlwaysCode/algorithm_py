import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    arr = ints()
    arr.sort()
    p, s = 0, 0
    for i in range(3):
        if arr[i] > 0:
            p += 1
        if arr[i] > 1 and arr[i-1] > 1:
            s += 1
            arr[i] -= 1
            arr[i-1] -= 1
    
    print(p + s)

t = int(input())
for _ in range(t):
    solve()
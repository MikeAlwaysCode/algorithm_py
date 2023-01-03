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
    arr = ints()

    ans, mx = 1, arr[0]
    for i, a in enumerate(arr[1:]):
        if a > mx:
            mx = a
            ans = i + 2

    print(ans)

t = int(input())
for _ in range(t):
    solve()
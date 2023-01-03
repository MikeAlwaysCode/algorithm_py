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
    cnt = collections.Counter(arr)

    ans = sum( v * (v - 1) // 2 for v in cnt.values() if v >= 2 )

    print(ans)

t = int(input())
for _ in range(t):
    solve()
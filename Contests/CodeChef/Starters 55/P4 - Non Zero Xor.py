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
    
    s = set([0])
    ans = 0
    xor = 0
    for i, a in enumerate(arr):
        xor ^= a
        # print(xor)
        if xor in s:
            # xor = 1 << mx
            # mx -= 1
            ans += 1
            s = set([xor])
        else:
            s.add(xor)
    print(ans)

t = int(input())
for _ in range(t):
    solve()
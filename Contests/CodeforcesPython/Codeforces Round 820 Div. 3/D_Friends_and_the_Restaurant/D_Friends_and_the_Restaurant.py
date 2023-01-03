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
    A = ints()
    B = ints()
    
    d = [y - x for x, y in zip(A, B)]
    d.sort()

    if d[-1] < 0:
        print(0)
        return
    
    l, r = 0, n - 1
    ans = 0
    while l < r:
        if d[l] + d[r] >= 0:
            ans += 1
            l += 1
            r -= 1
        else:
            l += 1
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()
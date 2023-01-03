from re import X
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
    
    cnt = 0
    cg = 0
    x = xi = yi = -1
    for i, a in enumerate(arr):
        # if a == 1:
        #     print(-1)
        #     return

        g = math.gcd(cg, a)
        if g == 1:
            cnt += 1
            if cnt > 1:
                print(-1)
                return
            x = a
            xi = i
        else:
            cg = g

    if cnt == 0:
        print(0)
        return

    cnt = 0
    cg = x
    for i, a in enumerate(arr):
        if i == xi:
            continue
        g = math.gcd(cg, a)
        if g == 1:
            cnt += 1
            if cnt > 1:
                print(-1)
                return
            yi = i
        else:
            cg = g

    if xi > yi:
        xi, yi = yi, xi
    ans = (xi != 0) + (yi != (n-1))
    print(ans)
    if xi != 0:
        print(1, xi + 1)
    if yi != n - 1:
        print(yi + 1, n)
            

t = int(input())
for _ in range(t):
    solve()
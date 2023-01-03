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
    arr = ints()

    if k == 1:
        print("Yes")
        return

    g = reduce(math.gcd, arr)

    cnt = 0
    cg = 0
    for a in arr:
        cg = math.gcd(cg, a)
        if cg == g:
            cnt += 1
            cg = 0
            
        if cnt >= k:
            print("Yes")
            return
    print("No")

t = int(input())
for _ in range(t):
    solve()
from re import A
import sys
import math
import collections
import random
from heapq import heapify, heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    A = ints()
    B = ints()

    ans = 0

    ha = []
    for a in A:
        heappush(ha, -a)
    hb = []
    for b in B:
        heappush(hb, -b)
    
    while ha:
        if ha[0] == hb[0]:
            heappop(ha)
            heappop(hb)
            continue
        ans += 1
        if ha[0] < hb[0]:
            mx = heappop(ha)
            heappush(ha, -len(str(-mx)))
        else:
            mx = heappop(hb)
            heappush(hb, -len(str(-mx)))

    print(ans)

t = int(input())
for _ in range(t):
    solve()
import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    chk = ints()
    
    ans = 1
    for i in range(22):
        k = 1 << i
        cnt = 0
        for n in chk:
            if n & k:
                cnt += 1
        if cnt == 1:
            ans = 0
            break
        elif cnt > 2:
            ans *= 4

    print(ans)

t = int(input())
for _ in range(t):
    solve()
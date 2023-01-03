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

    ans = 0
    for i, a in enumerate(arr):
        if i & 1:                   # 偶数坐标 视为可以取 Ai // 2个
            ans ^= (a // 2)
        else:                       # 奇数坐标
            ans ^= (a & 1)
            # if a & 1:               # Ai 是奇数
            #     ans ^= a
            # else:                   # Ai 是偶数
            #     ans ^= 1
            #     ans ^= (a - 1)
    print("CHEFINA" if ans == 0 else "CHEF")

t = int(input())
for _ in range(t):
    solve()
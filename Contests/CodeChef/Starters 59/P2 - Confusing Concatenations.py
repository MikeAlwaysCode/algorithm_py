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

    ans = [[] for _ in range(2)]

    idx, pre = 0, - 10 ** 6
    for a in arr:
        if a > pre:
            pre = a
            idx ^= 1
        ans[idx].append(a)
    if not ans[0] or not ans[1]:
        print(-1)
    else:
        for i in range(2):
            print(len(ans[i]))
            print(*ans[i])

t = int(input())
for _ in range(t):
    solve()
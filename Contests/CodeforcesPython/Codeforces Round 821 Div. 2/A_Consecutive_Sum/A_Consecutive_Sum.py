import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n, k = map(int, input().split())
    arr = ints()
    cnt = [-1] * k
    ans = 0
    for i, a in enumerate(arr):
        idx = i % k
        if cnt[idx] < 0:
            cnt[idx] = a
            ans += a
        elif a > cnt[idx]:
            ans += a - cnt[idx]
            cnt[idx] = a
    print(ans)

t = int(input())
for _ in range(t):
    solve()
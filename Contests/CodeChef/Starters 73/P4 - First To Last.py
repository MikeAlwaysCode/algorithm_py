import collections
import math
import random
import sys
from functools import *
from heapq import *

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n, m, k = map(int, input().split())
    spec = []
    for _ in range(k):
        spec.append(ints())

    if k == 0:
        print(n + m - 2)
        return

    rows, cols = map(set, zip(*spec))
    dr = {r:i for i, r in enumerate(sorted(rows))}
    dc = {c:i for i, c in enumerate(sorted(cols))}
    spec.sort()
    dp = [[1] * len(cols) for _ in range(len(rows))]
    for i in range(k):
        di = dr[spec[i][0]]
        dj = dc[spec[i][1]]
        if di > 0:
            dp[di][dj] = max(dp[di][dj], dp[di - 1][dj])
        if dj > 0:
            dp[di][dj] = max(dp[di][dj], dp[di][dj - 1])

    print(n + m - 2 - dp[len(rows) - 1][len(cols) - 1])

t = int(input())
for _ in range(t):
    solve()
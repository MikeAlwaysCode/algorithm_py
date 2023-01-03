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

def calFactor(x, m) -> int:
    cnt = 0
    while x % m == 0:
        cnt += 1
        x //= m
    return cnt

def solve() -> None:
    n, k = map(int, input().split())
    arr = ints()

    dp = [[-1] * (k * 25 + 1) for _ in range(k + 1)]

    dp[0][0] = 0
    for a in arr:
        cnt2 = cnt5 = 0
        while not a & 1:
            cnt2 += 1
            a >>= 1
        while a % 5 == 0:
            cnt5 += 1
            a //= 5
        for i in range(k, 0, -1):
            for j in range(k * 25, cnt5 - 1, -1):
                if dp[i-1][j-cnt5] >= 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-cnt5] + cnt2)

    ans = 0
    for i, cnt2 in enumerate(dp[k]):
        ans = max(ans, min(i, cnt2))
    print(ans)

t = 1
for _ in range(t):
    solve()
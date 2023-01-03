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
    n, m, b, MOD = map(int, input().split())
    arr = ints()

    dp = [[0] * (b + 1) for _ in range(m + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(1, m + 1):
            for k in range(arr[i], b + 1):
                dp[j][k] = (dp[j][k] + dp[j - 1][k - arr[i]]) % MOD
    
    ans = 0
    for v in dp[m]:
        ans = (ans + v) % MOD
    
    print(ans)

t = 1
for _ in range(t):
    solve()
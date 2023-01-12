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
    n = int(input())
    arr = ints()

    dp = [math.inf] * n
    mn = dp[0] = arr[0]
    for i in range(n):
        to = min(n - 1, i + arr[i])
        mx = max(mx, to)
        dp[to] = min(dp[to], dp[i] | arr[to])

    print(dp[n - 1])

t = int(input())
for _ in range(t):
    solve()
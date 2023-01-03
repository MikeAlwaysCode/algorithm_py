import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

MOD = 998244353

def solve() -> None:
    s = input()
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(1, n):
        dp[i+1] = dp[i]
        # if s[i-1:i+1] == "ab" or s[i-1:i+1] == "ba":
        if s[i] != s[i-1]:
            dp[i+1] += dp[i-1]
        dp[i+1] %= MOD
    
    print(dp[n])

t = int(input())
for _ in range(t):
    solve()
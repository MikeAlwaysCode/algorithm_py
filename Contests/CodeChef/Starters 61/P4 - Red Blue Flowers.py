import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    
    R = ints()
    B = ints()
    
    mx = 200 * n + 4
    dp = [-1] * mx
    dp[0] = 0

    for r, b in zip(R, B):
        for x in reversed(range(mx)):
            val = -1
            if dp[x] != -1:
                val = dp[x] + b
            if x - r >= 0 and dp[x-r] != -1:
                val = max(val, dp[x-r])
            dp[x] = val
    
    ans = 0
    for i in range(mx):
        if dp[i] == -1:
            continue
        ans = max(ans, min(i, dp[i]))
    print(ans)


t = int(input())
for _ in range(t):
    solve()
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
    s = input()
    n = len(s)

    ans = mx = cur = 0
    for i in range(n):
        subarrays = (i+1) * (n-i)
        if s[i] == '1':
            ans += subarrays
            subarrays *= -1
        cur += subarrays
        cur = max(cur, 0)
        mx = max(mx, cur)
    print(ans + mx)
    '''
    dp = [[0] * 3 for _ in range(n + 1)]
    for i in range(n):
        if s[i] == '1':
            nf, fl = (i + 1) * (n - i), 0
        else:
            fl, nf = (i + 1) * (n - i), 0

        dp[i + 1][0] = dp[i][0] + nf
        dp[i + 1][1] = max(dp[i][0] + fl, dp[i][1] + fl)
        dp[i + 1][2] = max(dp[i][1] + nf, dp[i][2] + nf)
        # dp[i + 1][3] = max(dp[i][0] + fl, dp[i][1] + fl)

    print(max(dp[n]))
    '''
t = int(input())
for _ in range(t):
    solve()
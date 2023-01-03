import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def comp(c, d) -> int:
    return -1 if c < d else 1 if c > d else 0

def solve() -> None:
    s = input().strip()
    n = len(s)

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1, 2):
        for l in range(n - length + 1):
            r = l + length
            dp[l][r] = 1

            res = -1
            if dp[l+1][r-1]:
                res = max(res, dp[l+1][r-1])
            else:
                res = max(res, comp(s[l], s[r-1]))
            
            if dp[l+2][r]:
                res = max(res, dp[l+2][r])
            else:
                res = max(res, comp(s[l], s[l+1]))

            dp[l][r] = min(dp[l][r], res)
            
            res = -1
            if dp[l+1][r-1]:
                res = max(res, dp[l+1][r-1])
            else:
                res = max(res, comp(s[r-1], s[l]))
            
            if dp[l][r-2]:
                res = max(res, dp[l][r-2])
            else:
                res = max(res, comp(s[r-1], s[r-2]))

            dp[l][r] = min(dp[l][r], res)
    
    if dp[0][n] == -1:
        print("Alice")
    elif dp[0][n]:
        print("Bob")
    else:
        print("Draw")
    
t = int(input())
for _ in range(t):
    solve()
import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n, m = map(int, input().split())
    n = min(n, m)
    print(ans[n])

inf = 10 ** 18
maxn = 5005
dp = [inf]*(maxn+1)
ans = [0]*(maxn+1)
dp[0] = 0
for i in range(1, maxn+1):
    for j in reversed(range(i, maxn+1)):
        dp[j] = min(dp[j], dp[j-i] + i*i)
    ans[i] = dp[i]

t = int(input())
for _ in range(t):
    solve()
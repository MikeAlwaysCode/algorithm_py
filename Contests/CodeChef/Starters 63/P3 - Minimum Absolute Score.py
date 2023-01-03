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
    A = input()
    B = input()

    ans = 0
    for i in range(n):
        ans += ord(A[i]) - ord(B[i]) + 26

    print(min(ans%26, (-ans)%26))

    '''
    dp = [[False] * 51 for _ in range(n + 1)]
    dp[0][25] = True

    for i in range(n):
        if A[i] == B[i]:
            p = s = 0
        else:
            p = (ord(B[i]) - ord(A[i])) % 26
            s = 26 - p
        # print(p, s)
        for j in range(51):
            if not dp[i][j]:
                continue
            if j + p < 51:
                dp[i+1][j+p] = True
            if j - s >= 0:
                dp[i+1][j-s] = True
    # print(dp)
    ans = 52
    for i in range(51):
        if dp[n][i]:
            ans = min(ans, abs(i-25))
    print(ans)
    '''

t = int(input())
for _ in range(t):
    solve()
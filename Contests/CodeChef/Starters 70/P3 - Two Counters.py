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
    n, m = map(int, input().split())
    time = ints()
    type = ints()

    dp = [[-1] * 5 for _ in range(m + 1)]
    dp[0][2] = 0
    pre = 0
    for i in range(m):
        shift = (time[i] - pre) & 1
        if shift:
            shift = min(3, time[i] - pre)
        else:
            shift = min(4, time[i] - pre)
        for j in range(5):
            if dp[i][j] == -1:
                continue
            for k in range(j - shift, j + shift + 1, 2):
                if k < 0 or k > 4:
                    continue

                if type[i] == 1:
                    if k > 2:
                        dp[i+1][k] = max(dp[i+1][k], dp[i][j] + 1)
                    # elif k == 2:
                    #     dp[i+1][k] = max(dp[i+1][k], dp[i][j])
                    else:
                        # dp[i+1][k] = max(dp[i+1][k], dp[i][j])
                        dp[i+1][2] = max(dp[i+1][2], dp[i][j])
                        # dp[i+1][k] = -1
                else:
                    if k < 2:
                        dp[i+1][k] = max(dp[i+1][k], dp[i][j] + 1)
                    # elif k == 2:
                    #     dp[i+1][k] = max(dp[i+1][k], dp[i][j])
                    else:
                        # dp[i+1][k] = max(dp[i+1][k], dp[i][j])
                        dp[i+1][2] = max(dp[i+1][2], dp[i][j])
                        # dp[i+1][k] = -1

        pre = time[i]

    print(max(dp[m]))

t = int(input())
for _ in range(t):
    solve()
import copy
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
    n, m = map(int, input().split())
    A = [0] * n
    B = [0] * n

    sumA = 0
    # C = [0] * n
    F = collections.defaultdict(int)

    for i in range(n):
        A[i], B[i] = map(int, input().split())
        sumA += A[i]
        # C[i] = B[i] - A[i]
        F[B[i] - A[i]] += 1
    
    INF = 10 ** 10
    dp = [INF] * (m + 1)
    dp[sumA] = 0

    # for c in C:
        # nxt = copy.copy(dp)
        # for i in range(m + 1):
        #     if 0 <= i + c <= m:
        #         nxt[i + c] = min(nxt[i + c], dp[i] + 1)
        # dp = nxt

    for c, f in F.items():
        if c == 0:
            continue
        
        x = 1
        while f:
            s = min(x, f)
            if c > 0:
                for i in reversed(range(m - c * s + 1)):
                    dp[i + c * s] = min(dp[i + c * s], dp[i] + s)
            else:
                for i in range(-c * s, m + 1):
                    dp[i + c * s] = min(dp[i + c * s], dp[i] + s)

            f -= s
            x *= 2
    
    for i in range(m + 1):
        if dp[i] == INF:
            print(-1)
        else:
            print(dp[i])
        

# t = int(input())
# for _ in range(t):
solve()
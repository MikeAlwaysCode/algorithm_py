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

def lis(nums, cmp = lambda x, y: x < y):
    P = [0] * len(nums)
    M = [0] * (len(nums) + 1)
    L = 0

    for i in range(len(nums)):
        lo, hi = 1, L

        while lo <= hi:
            mid = (lo + hi) // 2
            if cmp(nums[M[mid]], nums[i]):
                lo = mid + 1
            else:
                hi = mid - 1

        newL = lo
        P[i] = M[newL - 1]
        M[newL] = i

        L = max(L, newL)

    S = [0] * L
    k = M[L]

    for i in range(L - 1, -1, -1):
        S[i], k = nums[k], P[k]

    return S

def solve() -> None:
    n, m, k = map(int, input().split())
    spec = []
    for _ in range(k):
        x, y = map(int, input().split())
        if x < n and y < m:
            spec.append([x, y])
    
    ans = n + m - 2
    if spec:
        spec.sort(key=lambda x: (x[0], -x[1]))
        x, y = map(list, zip(*spec))
        ans -= len(lis(y))

    print(ans)

t = int(input())
for _ in range(t):
    solve()
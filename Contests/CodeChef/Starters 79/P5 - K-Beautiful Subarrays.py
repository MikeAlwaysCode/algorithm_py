import collections
import itertools
import math
import random
import sys
from functools import *
from heapq import *
from string import *

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n, m, k = map(int, input().split())
    arr = ints()

    # 阶乘
    fact = [1] * (n + m + 1)
    for i in range(1, n + m + 1):
        fact[i] = fact[i-1] * i % MOD

    # 逆元
    inverse = [0] * (n + m + 1)
    inverse[n + m] = pow(fact[n + m], MOD - 2, MOD)
    for i in range(n + m, 0, -1):
        inverse[i-1] = inverse[i] * i % MOD

    # 组合数
    def comb(n: int, m: int, MOD = MOD) -> int:
        if m < 0 or m > n:
            return 0
        return fact[n] * inverse[m] % MOD * inverse[n-m] % MOD

    
    if k == n:
        print(comb(n + m, m))
        return
    
    totc = 0
    clist = []
    for i in range(k):
        mx = cs = cnt = 0
        for j in range(i, n, k):
            cnt += 1
            mx = max(mx, arr[j])
            cs += arr[j]
        m -= mx * cnt - cs
        totc += cnt
        clist.append(cnt)

    if m < 0:
        print(0)
    elif m == 0:
        print(1)
    else:
        # for k in range()
        ans = comb(n - totc + m, m)
        for cnt in clist:
            ans += m // cnt
        print(ans % MOD)


for _ in range(int(input())):
# for _ in range(1):
    solve()
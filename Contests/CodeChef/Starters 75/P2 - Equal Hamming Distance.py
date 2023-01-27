import collections
import math
import random
import sys
from functools import *
from heapq import *

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    s1 = input()
    s2 = input()
    diff = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2: diff += 1
    
    if diff & 1:
        print(0)
        return
    
    # 阶乘
    fact = [1] * (diff + 1)
    for i in range(1, diff + 1):
        fact[i] = fact[i-1] * i % MOD
    # 逆元
    inverse = [0] * (diff + 1)
    inverse[diff] = pow(fact[diff], MOD - 2, MOD)
    for i in range(diff, 0, -1):
        inverse[i-1] = inverse[i] * i % MOD
    # 组合数
    def comb(n: int, m: int, MOD = MOD) -> int:
        if m < 0 or m > n:
            return 0
        return fact[n] * inverse[m] % MOD * inverse[n-m] % MOD
    
    ans = pow(2, n - diff, MOD) * comb(diff, diff//2) % MOD
    print(ans)

t = int(input())
for _ in range(t):
    solve()
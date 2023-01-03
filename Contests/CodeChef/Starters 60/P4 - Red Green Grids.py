import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

MOD = 998244353

def solve() -> None:
    n, m = map(int, input().split())
    
    k = n + m - 1
    if k & 1:
        print(0)
        return

    def comb(n: int, k: int) -> int:
        res = 1
        for i in range(1, k + 1):
            res = res * (n - i + 1) // i
        return res

    # ans = math.comb(k, k//2)
    ans = comb(k, k//2) % MOD
    ans *= pow(2, n * m - k, MOD)
    ans %= MOD

    k = min(n-1, m-1)
    # ans *= math.comb(n + m - 2, k)
    ans *= comb(n + m - 2, k)
    ans %= MOD

    print(ans)

t = int(input())
for _ in range(t):
    solve()
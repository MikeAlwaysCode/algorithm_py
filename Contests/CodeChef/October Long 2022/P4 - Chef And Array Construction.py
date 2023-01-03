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

    ans = 0
    right = 0
    for i in range(31):
        k = (m >> i) & 1
        l = m >> (i + 1)
        cnt = l * (1 << i)
        if k:
            cnt += right + 1
        
        ans += (1 << i) * pow(cnt, n, MOD)
        ans %= MOD

        if l == 0:
            break
        
        right += k << i
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()
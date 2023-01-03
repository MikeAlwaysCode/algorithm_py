import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    arr = ints()

    ans = 1
    cnt1 = 0
    odd = []
    for a in arr:
        if a == 1:
            cnt1 += 1
        elif a & 1:
            ans = (ans * a) % MOD
        else:
            odd.append(a)

    odd.sort()
    i = 0
    while i < len(odd) and cnt1:
        odd[i] ^= 1
        cnt1 -= 1
        i += 1
    
    for a in odd:
        ans = (ans * a) % MOD

    print(ans)

t = int(input())
for _ in range(t):
    solve()
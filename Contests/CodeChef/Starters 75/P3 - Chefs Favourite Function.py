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
    l, r = map(int, input().split())
    k = 1
    f = 0
    g = 1
    while k * 2 <= r:
        k *= 2
        f += 1
        g = g * 2 + 1

    def calf(x: int) -> int:
        f = 0
        while x:
            f += (x & 1) == 0
            x >>= 1
        return f
    if k >= l:
        ans = f + g
    else:
        g -= l - k
        ans = 0
        for i in range(31):
            if l + i > r: break
            ans = max(ans, g - i + calf(l + i))

    print(ans)


t = int(input())
for _ in range(t):
    solve()
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
    
    if k < l:
        g -= l - k
        if l & 1 and l + 1 <= r:
            l += 1
        f = 0
        while l:
            f += (l & 1) == 0
            l >>= 1

    print(f + g)


t = int(input())
for _ in range(t):
    solve()
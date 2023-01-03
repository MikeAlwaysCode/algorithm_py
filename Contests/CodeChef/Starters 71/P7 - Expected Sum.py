import collections
import math
import random
import sys
from functools import *
from heapq import *

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    a, b = map(int, input().split())

    n = a + b
    k = (n + 1) // 2

    # E = k * a / n

    print( k * a * pow(n, MOD - 2, MOD) % MOD)

t = int(input())
for _ in range(t):
    solve()
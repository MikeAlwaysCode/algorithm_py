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
    n, m = map(int, input().split())
    d = collections.Counter()
    ans = 0
    for _ in range(m):
        p, t = map(int, input().split())
        d[p] += t
        ans += d[p]
        print(ans)

# t = int(input())
# for _ in range(t):
solve()
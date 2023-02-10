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
    n, k = map(int, input().split())
    s = input()
    ans = 0
    d = [collections.Counter() for _ in range(26)]
    for i, c in enumerate(s):
        idx = ord(c) - 97
        keys = list(d[idx].keys())
        for key in keys:
            time, j = key
            d[idx][(time+2, j)] += 1
            d[idx][(time, j)] -= 1
        d[idx][(2, i)] += 1
        for j in range(26):
            time = 2
            while k + i + 1 - time >= 0:
                ans += d[j][(time, k + i + 1 - time)]
                time += 2
    print(ans)

t = int(input())
for _ in range(t):
    solve()
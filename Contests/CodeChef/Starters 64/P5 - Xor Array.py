import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    arr = ints()

    ans = 0
    q = [(0, n)]
    for bit in range(30):
        tmp = q
        q = []
        for l, r in tmp:
            left = l, right = l + 2
            

    return

t = int(input())
for _ in range(t):
    solve()
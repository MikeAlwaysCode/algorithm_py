import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    arr = ints()

    cnt = sum(a & 1 for a in arr)

    print("No" if cnt & 1 or cnt == 0 else "Yes")

t = int(input())
for _ in range(t):
    solve()
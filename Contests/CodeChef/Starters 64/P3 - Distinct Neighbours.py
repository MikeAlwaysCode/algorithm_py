import itertools
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

    if n == 1:
        print("Yes")
        return

    cnt = collections.Counter(arr)
    c1 = cnt.most_common(1)[0][1]

    if c1 - n > (n + 1) // 2:
        print("No")
    else:
        print("Yes")


t = int(input())
for _ in range(t):
    solve()
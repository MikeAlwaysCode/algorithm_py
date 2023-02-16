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
    arr = ints()
    arr.sort()
    if (arr[1] - arr[0]) & 1 or (arr[2] - arr[0]) & 1:
        print(-1)
    else:
        print((arr[1] + arr[2] - 2 * arr[0]) // 2)

t = int(input())
for _ in range(t):
    solve()
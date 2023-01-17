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
    n = int(input())
    arr = ints()

    s = 0
    ans = arr[0]
    for i, a in enumerate(arr):
        s += a
        ans = max(ans, (s + i) // (i + 1))

    print(ans)

t = int(input())
for _ in range(t):
    solve()
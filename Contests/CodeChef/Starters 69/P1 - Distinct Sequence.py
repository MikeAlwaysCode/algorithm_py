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
    s = input()

    cnt = s.count('1')
    if cnt == n * 2 or cnt == 0:
        print(-1)
        return

    if s[:n] != s[n:]:
        print(*list(range(1, n + 1)))
    else:
        print(*list(range(2, n + 2)))

t = int(input())
for _ in range(t):
    solve()
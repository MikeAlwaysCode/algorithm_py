import collections
import itertools
import math
import random
import sys
from functools import *
from heapq import *
from string import *

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    s = input()
    ans = xor = 0
    for c in s[:n - 1]:
        xor ^= int(c)
        if xor: ans += 1
    ans = max(ans, n - ans)
    print(ans)

for _ in range(int(input())):
# for _ in range(1):
    solve()
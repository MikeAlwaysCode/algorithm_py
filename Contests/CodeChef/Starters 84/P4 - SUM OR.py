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
MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    m = 0
    while n:
        m += n & 1
        n >>= 1
    if m < 3:
        print(0)
        return
    ans = (pow(3, m, MOD) - 3 * pow(2, m, MOD) + 3) % MOD
    print(ans)

for _ in range(int(input())):
# for _ in range(1):
    solve()
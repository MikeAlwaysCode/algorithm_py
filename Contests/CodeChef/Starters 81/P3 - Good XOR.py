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
    arr = ints()

    if n & 1:
        print(-1)
        return
    
    s = sum(arr)
    if s == 0 or (n == 2 and s != 1):
        print(-1)
    elif s <= n // 2:
        print(n // 2 - s)
    else:
        print((s - n // 2 + 1) // 2 + ((s - n // 2) & 1))

for _ in range(int(input())):
# for _ in range(1):
    solve()
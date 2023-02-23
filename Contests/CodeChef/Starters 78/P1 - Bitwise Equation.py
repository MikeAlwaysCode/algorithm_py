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
    
    if n == 0:
        print(5, 4, 3, 7)
    else:
        a = 1 << 33
        b = 1 << 35
        c = 3 << 33
        d = c + n
        print(a, b, c, d)

t = int(input())
for _ in range(t):
    solve()
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
    x = int(input())

    l, r = 1, 1001100000
    while l < r:
        m = l + r >> 1
        t = m * m
        p = int(pow(t, 1/3))
        while pow(p+1, 3) <= t:
            p += 1
        # t = p * p * p
        # k = int(math.sqrt(t))
        # while pow(k+1, 2) <= t:
        #     p += 1
        d = m - p
        if d >= x:
            r = m
        else:
            l = m + 1
    
    # print(r)
    print(r * r)
    

for _ in range(int(input())):
# for _ in range(1):
    solve()
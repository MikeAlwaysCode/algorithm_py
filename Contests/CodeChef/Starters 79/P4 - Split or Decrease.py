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

    tot = sum(arr)

    # s = tot & 1
    # f = (tot - n) & 1
    # print("CHEF" if f ^ s else "CHEFINA")
    
    s = 0
    for a in arr:
        s ^= (a == 1)
        if a & 1 == 0: s ^= 2
    print("CHEF" if s else "CHEFINA")

for _ in range(int(input())):
# for _ in range(1):
    solve()
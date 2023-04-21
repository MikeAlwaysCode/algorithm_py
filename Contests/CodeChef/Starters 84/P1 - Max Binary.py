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
    n, k = map(int, input().split())
    s = input()
    if s[0] == "0":
        s = "1" + s[1:] + "0" * (k - 1)
    else:
        s = s + "0" * k
    
    print(s)

for _ in range(int(input())):
# for _ in range(1):
    solve()
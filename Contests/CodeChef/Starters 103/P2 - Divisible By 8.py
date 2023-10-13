import math
import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from random import *
from string import *
from types import GeneratorType

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# print = lambda d: sys.stdout.write(str(d) + "\n")
# endregion fastio

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n, s = input().split()
    m = int(s[-3:])
    if m % 8 == 0:
        print(s)
    elif n == '1':
        print(8)
    else:
        for k in range(10):
            if (m // 10 * 10 + k) % 8 == 0:
                print(s[:int(n) - 1] + str(k))
                break

for _ in range(int(input())):
    solve()
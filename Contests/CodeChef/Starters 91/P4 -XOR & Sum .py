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
    l, r = mint()
    ans = 1 if l == 0 else 0
    for bit in range(60):
        k = pow(2, bit)
        if k > r: break
        if k < l: continue
        ans += k - l
    print(ans)

for _ in range(int(input())):
    solve()
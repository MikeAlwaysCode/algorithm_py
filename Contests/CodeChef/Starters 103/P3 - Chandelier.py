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
    n = sint()
    A = ints()
    B = ints()
    pres = [0] * (n + 1)
    suff = [0] * (n + 1)
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        suff[i] = max(suff[i + 1], B[i]) - A[i]
    for i in range(n):
        pres[i + 1] = max(pres[i], B[i]) - A[i]
        ans[i] = max(pres[i] + suff[i + 1], B[i]) - A[i]
    print(*ans)

for _ in range(int(input())):
    solve()
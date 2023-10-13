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
    n, k = mint()
    s = list(map(int, input()))
    cnt = [[0] * k for _ in range(2)]
    for i, c in enumerate(s):
        cnt[c][i % k] += 1
    ans = [0] * 2
    for i in range(k):
        ans[0] += cnt[1][i] // 2 + (cnt[1][i] & 1) * 2
        if ans[1] != math.inf:
            if cnt[1][i] == 0:
                ans[1] = math.inf
            else:
                ans[1] += cnt[0][i]
    print(min(ans))

for _ in range(int(input())):
    solve()
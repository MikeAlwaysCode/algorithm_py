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
    n, q = mint()
    arr = ints()
    cnt = [0] * (n + 1)
    for _ in range(q):
        l, r = mint()
        cnt[l - 1] += 1
        cnt[r] -= 1
    d = [0] * n
    cur = 0
    for i in range(n):
        cur += cnt[i]
        d[i] = cur
    arr.sort()
    idx = sorted(range(n), key = lambda x: d[x])
    s = 0
    ans = [0] * n
    for i, p in enumerate(idx):
        ans[p] = arr[i]
        s += arr[i] * d[p]
    print(s)
    print(*ans) 

for _ in range(int(input())):
    solve()
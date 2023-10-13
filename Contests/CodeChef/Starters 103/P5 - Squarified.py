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

mxn = 10 ** 7
factor = [1] * (mxn + 1)
primes = list()
def init():
    for i in range(2, mxn + 1):
        if factor[i] != 1:
            continue
        primes.append(i)
        for j in range(i, mxn + 1, i):
            factor[j] = i
def prime_factor(x):
    cnt = Counter()
    while x != 1:
        cnt[factor[x]] += 1
        x //= factor[x]
    res = 1
    for k, v in cnt.items():
        if v & 1:
            res *= k
    return res

def solve() -> None:
    n = sint()
    nums = ints()
    cnt = Counter()
    ans = 0
    for x in nums:
        x = prime_factor(x)
        if x > 1:
            cnt[x] += 1
            ans = max(ans, cnt[x])
    print(ans)

init()
for _ in range(int(input())):
    solve()
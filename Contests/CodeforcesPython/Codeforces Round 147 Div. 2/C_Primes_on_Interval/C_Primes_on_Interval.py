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

# # region interactive
# def printQry(a, b) -> None:
#     sa = str(a)
#     sb = str(b)
#     print(f"? {sa} {sb}", flush = True)

# def printAns(ans) -> None:
#     s = str(ans)
#     print(f"! {s}", flush = True)
# # endregion interactive

# # region dfsconvert
# def bootstrap(f, stack=[]):
#     def wrappedfunc(*args, **kwargs):
#         if stack:
#             return f(*args, **kwargs)
#         else:
#             to = f(*args, **kwargs)
#             while True:
#                 if type(to) is GeneratorType:
#                     stack.append(to)
#                     to = next(to)
#                 else:
#                     stack.pop()
#                     if not stack:
#                         break
#                     to = stack[-1].send(to)
#             return to
#     return wrappedfunc
# # endregion dfsconvert

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    a, b, k = mint()

    # 1. 求a - b之间的质数列表
    factor = [1] * (b + 1)
    primes = [a - 1]    # 哨兵
    for i in range(2, b + 1):
        if factor[i] != 1: continue
        if i >= a:
            primes.append(i)
        for j in range(i, b + 1, i):
            factor[j] = i

    # print(primes)
    if len(primes) < k + 1:
        print(-1)
        return
    ans, p = b - a + 1, 0
    for l in range(len(primes) - k):
        r = l + k   # l - r有k + 1个质数
        # 2. x的范围为a - primes[l + 1], 可使得从x到primes[r]之间有k个质数
        # 3. primes[l + 1] = b - L + 1, L = b - primes[l + 1] + 1
        # 4. 从primes[l]到primes[l + 1]的范围的数，要满足有k个点的最小L为：primes[r] - primes[l]
        p = max(p, primes[r] - primes[l])
        ans = min(ans, max(b - primes[l + 1] + 1, p))
    print(ans)

# for _ in range(int(input())):
solve()
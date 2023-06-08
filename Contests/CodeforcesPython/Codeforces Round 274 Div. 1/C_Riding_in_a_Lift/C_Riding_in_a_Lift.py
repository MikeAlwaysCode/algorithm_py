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
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, a, b, k = mint()
    # 1. 1 ≤ y ≤ n
    # 2. y ≠ x
    # 3. y ≠ b
    # 4. |x - y| < |x - b|

    # 使得计算1, a, b
    if a > b: a, b = n + 1 - a, n + 1 - b

    '''
    # k等于1的情况下，b+n有(n - 1) * 2个方案
    @cache
    def dfs(a: int, k: int) -> int:
        nonlocal b
        l, r = a - 1, n - a

        if k == 1:
            c = abs(a - b) - 1
            return min(r, c) + min(l, c)

        res = 0
        for i in range(1, abs(a - b)):
            if a - i >= 1:
                res += dfs(a - i, k - 1)
            if a + i <= n:
                res += dfs(a + i, k - 1)
        return res
    print(dfs(a, k))
    '''
    dp = [0] * b
    dp[a] = 1
    for _ in range(k):
        pres = list(accumulate(dp))
        for i in range(1, b):
            # x <= (b + y - 1) // 2
            dp[i] = (pres[(b + i - 1) // 2] - dp[i]) % MOD
    print(sum(dp) % MOD)

# for _ in range(int(input())):
solve()
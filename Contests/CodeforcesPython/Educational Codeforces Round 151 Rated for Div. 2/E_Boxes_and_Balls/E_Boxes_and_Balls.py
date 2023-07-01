from bisect import bisect, bisect_left
import sys

# import itertools
# import math
# import os
# import random
# from collections import *
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from io import BytesIO, IOBase
# from string import *

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
# from types import GeneratorType
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
    n, k = mint()
    nums = ints()
    less = sum(nums) <= n // 2
    pos = [i for i, x in enumerate(nums) if x == less]
    dp = [[0] * (k + 1) for _ in range(len(pos) + 1)]
    dp[0][0] = 1
    for i in range(n):
        j0 = bisect_left(pos, i)
        for j in range(min(i + 1, len(pos), j0 + 40), max(0, j0 - 40), -1):
            d = abs(pos[j - 1] - i)
            for t in range(k, d - 1, -1):
                dp[j][t] = (dp[j][t] + dp[j - 1][t - d]) % MOD
    print(sum(dp[-1][i] for i in range(k, -1, -2)) % MOD)

# for _ in range(int(input())):
solve()
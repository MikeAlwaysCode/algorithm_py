import sys

# import itertools
# import math
# import os
# import random
# from bisect import bisect, bisect_left
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
    nums.sort()

    # dp[i][j]：最后一组最小元素i差是j
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[1][0] = dp[0][0] = 1
    for i in range(1, n):
        tmp = [[0] * (k + 1) for _ in range(n + 1)]
        for j in range(i + 1):
            t = j * (nums[i] - nums[i - 1])
            for l in range(k - t + 1):
                # Continuing
                tmp[j][l + t] = (tmp[j][l + t] + dp[j][l] * j) % MOD
                # Starting
                if j < n:
                    tmp[j + 1][l + t] = (tmp[j + 1][l + t] + dp[j][l]) % MOD
                # Closing
                if j:
                    tmp[j - 1][l + t] = (tmp[j - 1][l + t] + dp[j][l] * j) % MOD
                # Open and close
                tmp[j][l + t] = (tmp[j][l + t] + dp[j][l]) % MOD

        dp = tmp

    print(sum(dp[0]) % MOD)

solve()
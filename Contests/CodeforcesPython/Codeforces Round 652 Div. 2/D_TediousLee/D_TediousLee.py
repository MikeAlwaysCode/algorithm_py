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

mx = 2 * 10 ** 6

'''
# 1123 ms
dp = [[0] * 4 for _ in range(mx + 1)]
dp[1][0] = 1
for i in range(2, mx + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] * 2) % MOD
    dp[i][1] = dp[i - 1][0]
    dp[i][2] = dp[i - 1][1]
    dp[i][3] = (dp[i][2] * 4 + dp[i - 3][3]) % MOD

def solve() -> None:
    n = sint()

    print(dp[n][3])
'''

'''
# 108ms
dp = [0] * (mx + 1)
dp[3] = dp[4] = 4
for i in range (5, mx + 1):
    dp[i] = max(((2 * dp[i-2]) + dp[i-1]) % MOD, ((4 * dp[i-4]) + 4 * dp[i-3] + dp[i-2] + 4) % MOD)
    
def solve() -> None:
    n = sint()
    print(dp[n])
'''

for _ in range(int(input())):
    solve()
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
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, k = mint()
    s = list(map(int, list(input())))
    cnt0 = s.count(0)
    cnt1 = n - cnt0
    x1 = y1 = x2 = y2 = 0
    dp0 = [[0] * 2 for _ in range(k + 1)]
    dp1 = [[0] * 2 for _ in range(k + 1)]
    for i, c in enumerate(s):
        ndp0 = [[0] * 2 for _ in range(k + 1)]
        ndp1 = [[0] * 2 for _ in range(k + 1)]
        ndp0[0][c] = dp0[0][c] + 1
        ndp0[0][c ^ 1] = 0
        ndp1[0][c] = dp1[0][c] + 1
        ndp1[0][c ^ 1] = 0

        if ndp0[0][0] > x2 or (ndp0[0][0] == x2 and ndp0[0][1] > y2):
            x2, y2 = ndp0[0][0], ndp0[0][1]
        if ndp1[0][0] > x2 or (ndp1[0][0] == x2 and ndp1[0][1] > y2):
            x2, y2 = ndp1[0][0], ndp1[0][1]
        
        if sum(ndp0[0]) > x1 + y1:
            x1, y1 = ndp0[0][0], ndp0[0][1]
        if sum(ndp1[0]) > x1 + y1:
            x1, y1 = ndp1[0][0], ndp1[0][1]
        
        for j in range(1, k + 1):
            if c == 0:
                ndp0[j][c] = dp0[j][c] + 1
                ndp0[j][c ^ 1] = 0
                ndp1[j][c] = 0
                ndp1[j][c ^ 1] = dp1[j - 1][c] + 1
            else:
                ndp0[j][c] = 0
                ndp0[j][c ^ 1] = dp0[j - 1][c ^ 1] + 1
                ndp1[j][c] = dp1[j][c] + 1
                ndp1[j][c ^ 1] = 0

            if ndp0[j][0] > x2 or (ndp0[j][0] == x2 and ndp0[j][1] > y2):
                x2, y2 = ndp0[j][0], ndp0[j][1]
            if ndp1[j][0] > x2 or (ndp1[j][0] == x2 and ndp1[j][1] > y2):
                x2, y2 = ndp1[j][0], ndp1[j][1]
            if sum(ndp0[j]) > x1 + y1:
                x1, y1 = ndp0[j][0], ndp0[j][1]
            if sum(ndp1[j]) > x1 + y1:
                x1, y1 = ndp1[j][0], ndp1[j][1]
        
        dp0, dp1 = ndp0, ndp1
                
    print(x1, y1, x2, y2)

for _ in range(int(input())):
    solve()
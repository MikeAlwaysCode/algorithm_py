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
    n = sint()
    g = []
    dia1 = [0] * (n * 2)
    dia2 = [0] * (n * 2)
    for i in range(n):
        g.append(ints())
        for j, x in enumerate(g[-1]):
            dia1[i + j] += x
            dia2[i - j + n] += x
    
    ans = [-1] * 2
    x = [-1] * 2
    y = [-1] * 2
    for i in range(n):
        for j in range(n):
            c = (i + j) & 1
            res = dia1[i + j] + dia2[i - j + n] - g[i][j]
            if res > ans[c]:
                ans[c], x[c], y[c] = res, i + 1, j + 1
    print(sum(ans))
    print(x[0], y[0], x[1], y[1])


solve()
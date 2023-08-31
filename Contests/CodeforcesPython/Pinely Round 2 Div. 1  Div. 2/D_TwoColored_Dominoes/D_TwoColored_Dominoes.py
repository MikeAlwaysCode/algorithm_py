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
    n, m = mint()
    row = dict()
    col = dict()
    g = [['.'] * m for _ in range(n)]
    for i in range(n):
        s = input()
        for j, c in enumerate(s):
            if c == "L":
                r1, c1, c2 = i, j, j + 1
                if (c1, c2) in row:
                    r2 = row[(c1, c2)]
                    del row[(c1, c2)]
                    g[r1][c1] = 'W'
                    g[r1][c2] = 'B'
                    g[r2][c1] = 'B'
                    g[r2][c2] = 'W'
                else:
                    row[(c1, c2)] = r1
            if c == 'U':
                r1, r2, c1 = i, i + 1, j
                if (r1, r2) in col:
                    c2 = col[(r1, r2)]
                    del col[(r1, r2)]
                    g[r1][c1] = 'W'
                    g[r1][c2] = 'B'
                    g[r2][c1] = 'B'
                    g[r2][c2] = 'W'
                else:
                    col[(r1, r2)] = c1
    if len(row) or len(col):
        print(-1)
    else:
        for row in g:
            print("".join(row))

for _ in range(int(input())):
    solve()
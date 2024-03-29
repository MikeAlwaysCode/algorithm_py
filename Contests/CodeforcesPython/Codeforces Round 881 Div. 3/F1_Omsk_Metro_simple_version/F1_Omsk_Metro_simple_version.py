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
    mx = [0] * (n + 2)
    mn = [0] * (n + 2)
    emx = [0] * (n + 2)
    emn = [0] * (n + 2)
    mx[1] = emx[1] = 1
    cur = 2
    for _ in range(n):
        qry = input().split()
        if qry[0] == "+":
            u, x = int(qry[1]), int(qry[2])
            emx[cur] = max(emx[u] + x, x)
            emn[cur] = min(emn[u] + x, x)
            mx[cur] = max(mx[u], emx[cur])
            mn[cur] = min(mn[u], emn[cur])
            cur += 1
        else:
            u, v, x = int(qry[1]), int(qry[2]), int(qry[3])
            print("YES" if mn[v] <= x <= mx[v] else "NO")

for _ in range(int(input())):
    solve()
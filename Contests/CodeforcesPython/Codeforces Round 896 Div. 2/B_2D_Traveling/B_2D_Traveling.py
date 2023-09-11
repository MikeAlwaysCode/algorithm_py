import math
import sys

# import itertools
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
    n, k, a, b = mint()
    a -= 1
    b -= 1
    city = []
    for _ in range(n):
        city.append(tuple(mint()))
    if a < k and b < k:
        print(0)
        return
    def f(i: int, j: int) -> int:
        if i < k and j < k:
            return 0
        return abs(city[i][0] - city[j][0]) + abs(city[i][1] - city[j][1])
    ans = f(a, b)
    
    resa = resb = math.inf
    for i in range(k):
        resa = min(resa, f(i, a))
        resb = min(resb, f(i, b))
    ans = min(ans, resa + resb)
    print(ans)

for _ in range(int(input())):
    solve()
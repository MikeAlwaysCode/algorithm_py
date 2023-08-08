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

MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, s = mint()
    edges = [tuple(mint()) for _ in range(n - 1)]
    edges.sort(key = lambda x: x[2])

    fa = list(range(n))
    sz = [1] * n
    def find(x: int) -> int:
        cur = x
        while fa[x] != x:
            x = fa[x]
        while fa[cur] != x:
            fa[cur], cur = x, fa[cur]
        return x
    def union(x: int, y: int):
        if sz[x] > sz[y]:
            x, y = y, x
        sz[y] += sz[x]
        fa[x] = y
    
    ans = 1
    for u, v, w in edges:
        fu, fv = find(u - 1), find(v - 1)
        if fu != fv:
            ans = (ans * pow(s - w + 1, sz[fu] * sz[fv] - 1, MOD)) % MOD
            union(fu, fv)
    print(ans)

for _ in range(int(input())):
    solve()
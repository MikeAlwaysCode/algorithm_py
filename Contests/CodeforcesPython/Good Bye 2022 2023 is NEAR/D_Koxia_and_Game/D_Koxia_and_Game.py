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
    n = sint()
    A = ints()
    B = ints()
 
    fa = list(range(n + 1))
    cnt_v = [1] * (n + 1)
    cnt_e = [0] * (n + 1)
    self_loop = [False] * (n + 1)
    def find(x: int):
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            fa[cur], cur = x, fa[cur]
        return x

    def union(x: int, y: int):
        fx, fy = find(x), find(y)
        cnt_e[fy] += 1
        if x == y: self_loop[fx] = True
        if fx == fy: return
        self_loop[fy] |= self_loop[fx]
        cnt_v[fy] += cnt_v[fx]
        cnt_e[fy] += cnt_e[fx]
        fa[fx] = fy

    for u, v in zip(A, B):
        union(u, v)
        
    ans = 1
    for i in range(1, n + 1):
        fi = find(i)
        if fi != i: continue
        if cnt_e[i] != cnt_v[i]:
            print(0)
            return
        if self_loop[i]:
            ans = ans * n % MOD
        else:
            ans = ans * 2 % MOD

    print(ans)

for _ in range(int(input())):
    solve()

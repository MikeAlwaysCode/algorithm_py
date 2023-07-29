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
    nums = ints()
    f = [0] * (n + 1)
    g = [0] * (n + 3)
    l = [0] * (n + 1)
    ans = 0
    for x in nums:
        if x == 0:
            f[0] = (f[0] * 2 + 1) % MOD
        else:
            if x == 1:
                ans = (ans * 2 + 1) % MOD
            else:
                g[x] = (g[x] * 2 + l[x - 2] + f[x - 2]) % MOD
            f[x] = (f[x] * 2 + f[x - 1]) % MOD
        l[x] = (l[x] * 2 + g[x + 2]) % MOD
    ans = (ans + sum(f) + sum(g) + sum(l)) % MOD
    print(ans)


for _ in range(int(input())):
    solve()
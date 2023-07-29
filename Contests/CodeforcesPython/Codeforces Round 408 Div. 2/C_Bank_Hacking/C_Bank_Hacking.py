import math
import sys
from heapq import heapify, heappop, heappush

# import itertools
# import math
# import os
# import random
# from bisect import bisect, bisect_left
# from collections import *
# from functools import reduce
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
    nums = ints()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    h = [(-x, i) for i, x in enumerate(nums)]
    h_del, h_add = [], []
    heapify(h)
    ans = math.inf
    for i in range(n):
        res = nums[i]
        h_del.clear()
        h_add.clear()
        h_del.append((-nums[i], i))
        for j in g[i]:
            res = max(res, nums[j] + 1)
            h_del.append((-nums[j], j))
        heapify(h_del)
        while h_del and h[0][1] == h_del[0][1]:
            h_add.append(h[0][1])
            heappop(h_del)
            heappop(h)
        if h: res = max(res, 2 - h[0][0])
        ans = min(ans, res)
        for x in h_add:
            heappush(h, (-nums[x], x))
    print(ans)

solve()
import sys
import itertools
from bisect import bisect, bisect_left

# import math
# import os
# import random
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
    n, c = mint()
    nums = ints()
    left = [0] * n
    # right = [0] * n
    mn = [0] * n
    for i in range(n):
        l, r = nums[i] + i + 1, nums[i] + n - i
        # left[i], right[i] = l, r
        left[i] = l
        mn[i] = min(l, r)

    ans = 0
    idx = sorted(range(n), key = lambda x: mn[x])
    d = {x:i for i, x in enumerate(idx)}
    pres = list(itertools.accumulate(sorted(mn)))
    for i in range(n):
        if c < left[i]: continue
        cc = c - left[i]
        j = bisect(pres, cc)
        if d[i] < j:
            j = bisect(pres, cc + mn[i])
            ans = max(ans, j)
        else:
            ans = max(ans, j + 1)

    print(ans)

for _ in range(int(input())):
    solve()
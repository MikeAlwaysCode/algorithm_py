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
    l = ints()
    mx, mn = [0] * (m + 1), [0] * (m + 1)
    for i in range(m - 1, -1, -1):
        mx[i] = mx[i + 1] + l[i]
        mn[i] = max(l[i], mn[i + 1] + 1)
        if mn[i] + i > n:
            print(-1)
            return
    
    if mx[0] < n:
        print(-1)
        return
    
    ans = [1] * m
    for i in range(1, m):
        if n - ans[i - 1] - l[i - 1] + 1 > mn[i]:
            ans[i] = ans[i - 1] + l[i - 1]
        else:
            ans[i] = max(ans[i - 1] + 1, n - mn[i] + 1)
    print(*ans)

solve()
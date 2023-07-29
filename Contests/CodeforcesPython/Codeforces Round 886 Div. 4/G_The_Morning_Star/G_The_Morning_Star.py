import sys
from typing import Counter

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
    ans = 0
    cnt = Counter()
    for _ in range(n):
        x, y = mint()
        ans += cnt[(1, x)] + cnt[(2, y)] + cnt[(3, x + y)] + cnt[(4, x - y)]
        cnt[(1, x)] += 1
        cnt[(2, y)] += 1
        cnt[(3, x + y)] += 1
        cnt[(4, x - y)] += 1
    '''
    # x1 == x2
    cntx = Counter()
    # y1 == y2
    cnty = Counter()
    # y1 - y2 == x2 - x1 -> x1 + y1 == x2 + y2
    cntp = Counter()
    # y2 - y1 == x2 - x1 -> x1 - y1 == x2 - y2
    cnts = Counter()

    for _ in range(n):
        x, y = mint()
        ans += cntx[x] + cnty[y] + cntp[x + y] + cnts[x - y]
        cntx[x] += 1
        cnty[y] += 1
        cntp[x + y] += 1
        cnts[x - y] += 1
    '''
    print(ans * 2)

for _ in range(int(input())):
    solve()


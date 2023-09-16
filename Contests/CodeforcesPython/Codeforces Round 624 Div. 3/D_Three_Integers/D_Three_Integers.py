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
    a, b, c = mint()
    ans = math.inf
    aa = ab = ac = -1
    for x in range(1, a * 2 + 1):
        da = abs(x - a)
        for y in range(x, b * 2 + 1, x):
            db = abs(y - b)
            if da + db >= ans: continue
            z = (c + y // 2) // y * y
            res = da + db + abs(z - c)
            '''
            m = c // y
            for zz in range(2):
                z = (m + zz) * y
                res = da + db + abs(z - c)
            '''
            if res < ans:
                ans = res
                aa, ab, ac = x, y, z
    print(ans)
    print(aa, ab, ac)

for _ in range(int(input())):
    solve()
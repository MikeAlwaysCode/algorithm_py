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
    n, k = mint()
    s = list(input())
    l = ints()
    r = ints()
    q = sint()
    xs = ints()
    xs.sort()
    rev = [0] * (n + 1)
    i = 0
    for x in xs:
        while x > r[i]:
            i += 1
        a, b = min(x, l[i] + r[i] - x), max(x, l[i] + r[i] - x)
        rev[a - 1] += 1
        rev[b] -= 1
    # print(rev)
    d = i = 0
    for j in range(n):
        d = (d + rev[j]) & 1
        while j + 1 > r[i]:
            i += 1
        if d and (j + 1) * 2 < l[i] + r[i]:
            x = l[i] + r[i] - j - 2
            s[j], s[x] = s[x], s[j]
    print("".join(s))

for _ in range(int(input())):
    solve()
import math
import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from random import *
from string import *
from types import GeneratorType

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
    h, c, t = mint()
    if h <= t:
        print(1)
    elif h + c >= t * 2:
        print(2)
    else:
        # n = (h - c) // (2 * t - h - c)
        n = (2 * t - 2 * c - 1) // (2 * t - h - c)
        if not n & 1:
            m = n // 2
            v1 = abs(((m + 1) * h + m * c) * (n - 1) - t * (n + 1) * (n - 1))
            v2 = abs((m * h + (m - 1) * c) * (n + 1) - t * (n + 1) * (n - 1))
            n = n + 1 if v1 < v2 else n - 1
        print(n)

for _ in range(int(input())):
    solve()
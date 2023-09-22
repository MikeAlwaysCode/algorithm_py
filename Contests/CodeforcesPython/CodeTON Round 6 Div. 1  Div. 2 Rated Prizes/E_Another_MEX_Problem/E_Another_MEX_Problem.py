import math
import sys
from collections import *

# import itertools
# import os
# import random
# from bisect import bisect, bisect_left
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from io import BytesIO, IOBase
# from string import *

# region fast io
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))


# print = lambda d: sys.stdout.write(str(d) + "\n")
# endregion fast io

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
    nums = [math.inf] + ints()
    ok = Counter()
    ok[0] = 1
    mex = [0]
    s = [0] * (n + 5)
    s[1] = 1
    u = [0] * (n + 5)
    y = [0] * (n + 5)
    for r in range(1, n + 1):
        m, z = 0, []
        for l in range(r, 0, -1):
            u[nums[l]] = r
            while u[m] == r:
                m += 1
            if y[m] >= l:
                continue
            for i in range(s[y[m]], s[l]):
                v = m ^ mex[i]
                if not ok[v]:
                    ok[v] = 1
                    z.append(v)
            y[m] = l
        for i in z:
            mex.append(i)
        s[r + 1] = len(mex)
    for x in range(n, -1, -1):
        if ok[x]:
            print(x)
            return

for _ in range(sint()):
    solve()

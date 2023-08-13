import sys
from functools import reduce
from operator import mul

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
    nums = ints()
    mxn = max(nums)
    factor = [0 if i % 2 else 2 for i in range(mxn + 1)]
    for i in range(2, mxn + 1):
        if factor[i]:
            continue
        for j in range(i, mxn + 1, i):
            factor[j] = i
    def prime_factor(x):
        res = set()
        while x != 1:
            res.add(factor[x])
            x //= factor[x]
        return res
            
    ans = [[-1] * n for _ in range(2)]

    for i, x in enumerate(nums):
        res = list(prime_factor(x))

        if len(res) > 1:
            ans[0][i], ans[1][i] = res[0], reduce(mul, res[1:])

    for a in ans:
        print(*a)

solve()
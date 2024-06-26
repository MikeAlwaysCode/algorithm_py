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
    nums = ints()

    def check(x: int) -> bool:
        cnt = 0
        for i in range(n):
            if nums[i] * 2 < x:
                cnt += 1
        if cnt > k:
            return False
        elif cnt <= k - 2:
            return True

        for i in range(n - 1):
            a, b = nums[i], nums[i + 1]
            if a * 2 < x:
                a = 10 ** 9
            if b * 2 < x:
                b = 10 ** 9
            if a >= x and b >= x:
                return True
            if k > cnt and (a >= x or b >= x):
                return True
        return False

    l, r = 0, 10 ** 9
    while l < r:
        mid = (l + r + 1) >> 1
        if check(mid):
            l = mid
        else:
            r = mid - 1
    print(l)

for _ in range(int(input())):
    solve()
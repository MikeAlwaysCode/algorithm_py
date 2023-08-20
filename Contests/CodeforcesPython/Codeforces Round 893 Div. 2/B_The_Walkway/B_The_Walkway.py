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
    n, m, d = mint()
    nums = [1] + ints()
    cnt = [0] * (m + 1)
    cnt[0] = 1
    for i in range(1, m + 1):
        cnt[i] = cnt[i - 1] + (nums[i] - nums[i - 1] + d - 1) // d
    mn = last = cnt[-1] + (n - nums[-1]) // d
    ans = 0

    # print(cnt)
    for i in range(1, m + 1):
        cur = cnt[i - 1]
        if i == m:
            cur += (n - nums[i - 1]) // d
        else:
            cur += last - cnt[i + 1] + (nums[i + 1] - nums[i - 1] + d - 1) // d
        if cur < mn:
            mn = cur
            ans = 1
        elif cur == mn:
            ans += 1

    print(mn, ans)

for _ in range(int(input())):
    solve()
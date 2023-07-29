import math
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
    n = sint()
    nums = ints()

    # greedy
    ans = l = 0
    while l < n:
        r = l + 1
        hasTwo = (nums[l] == 2)
        hasMiddleZero = False
        while r < n:
            if r - 1 > l and nums[r - 1] == 0:
                hasMiddleZero = True
            if nums[r] == 2:
                hasTwo = True
            if hasMiddleZero or (nums[l] == 0 and nums[r] == 0 and not hasTwo):
                break
            r += 1
        l = r
        ans += 1
    print(ans)

    '''
    # dp 249 ms
    dp = [[math.inf] * 3 for _ in range(n + 1)]
    dp[0][0] = 0
    for i, x in enumerate(nums):
        dp[i + 1][x] = min(dp[i]) + 1
        if dp[i][1] != math.inf:
            dp[i + 1][x] = min(dp[i + 1][x], dp[i][1])
        if dp[i][2] != math.inf:
            dp[i + 1][x] = min(dp[i + 1][x], dp[i][2])
        if x and i >= 1:
            dp[i + 1][x - 1] = min(dp[i - 1]) + 1
            if nums[i - 1]: dp[i + 1][x - 1] = min(dp[i + 1][x - 1], dp[i][nums[i - 1] - 1])

    # print(dp)
    print(min(dp[-1]))
    '''

solve()
import math
import sys
# from functools import cache

# import itertools
# import math
# import os
# import random
# from bisect import bisect, bisect_left
# from collections import *
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
    s = input()

    n = len(s)
    c0 = s.count('0')
    c1 = n - c0
    # 全部可能 - count("00") + count("11") = count("01") + count("10") + 2 * count("11")
    target = (n * (n - 1) // 2 - c0 * (c0 - 1) // 2 + c1 * (c1 - 1) // 2) // 2
    dp = [[math.inf] * (target + 1) for _ in range(c1 + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(min(c1 - 1, i), -1, -1):
            for k in range(target - i + 1):
                # s[i]若是1，"01" + "11"将增加i
                dp[j + 1][k + i] = min(dp[j + 1][k + i], dp[j][k] + int(s[i] == '0'))
    
    print(dp[c1][target])

    '''
    if s.count('0') & 1:
        pos = [i for i, c in enumerate(s) if c == '0']
    else:
        pos = [i for i, c in enumerate(s) if c == '1']
    # print(pos)
    n = len(s)
    target = (n - 1) * len(pos) // 2
    
    def f(nums: list, i: int, cost: int) -> int:
        nonlocal target
        tot = sum(nums)
        if tot == target:
            return cost
        if i == len(nums):
            return len(nums) + 1
        res = f(nums, i + 1, cost)
        ss = set(nums)
        x = nums[i]
        for y in range(len(nums)):
            if tot + y - x > target: break
            if y != x and y not in ss:
                nums[i] = y
                res = min(res, f(nums, i + 1, cost + 1))
        nums[i] = x
        return res
    print(f(pos, 0, 0))
    '''

solve()
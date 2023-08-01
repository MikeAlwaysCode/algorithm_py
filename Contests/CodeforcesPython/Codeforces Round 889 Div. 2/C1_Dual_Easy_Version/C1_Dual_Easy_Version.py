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
    mx, mn = max(nums), min(nums)
    ans = []
    if mx <= 0:
        for i in range(n - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                nums[i - 1] += nums[i]
                ans.append((i, i + 1))
    elif mn >= 0:
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                nums[i] += nums[i - 1]
                ans.append((i + 1, i))
    else:
        neg = pos = 0
        for x in nums:
            if x > 0: pos += 1
            elif x < 0: neg += 1
        if min(neg, pos) >= 8:
            if mx >= abs(mn):
                idx = nums.index(mx)
                for i in range(n):
                    if nums[i] < 0:
                        nums[i] += mx
                        ans.append((i + 1, idx + 1))
                for i in range(1, n):
                    if nums[i] < nums[i - 1]:
                        nums[i] += nums[i - 1]
                        ans.append((i + 1, i))
            else:
                idx = nums.index(mn)
                for i in range(n):
                    if nums[i] > 0:
                        nums[i] += mn
                        ans.append((i + 1, idx + 1))
                for i in range(n - 1, 0, -1):
                    if nums[i] < nums[i - 1]:
                        nums[i - 1] += nums[i]
                        ans.append((i, i + 1))
        else:
            if pos < neg:
                idx = nums.index(mn)
                while mx + mn > 0:
                    ans.append((idx + 1, idx + 1))
                    mn *= 2
                    nums[idx] *= 2
                for i in range(n):
                    if nums[i] > 0:
                        ans.append((i + 1, idx + 1))
                        nums[i] += mn
                for i in range(n - 1, 0, -1):
                    if nums[i] < nums[i - 1]:
                        nums[i - 1] += nums[i]
                        ans.append((i, i + 1))
            else:
                idx = nums.index(mx)
                while mx + mn < 0:
                    ans.append((idx + 1, idx + 1))
                    mx *= 2
                    nums[idx] *= 2
                for i in range(n):
                    if nums[i] < 0:
                        ans.append((i + 1, idx + 1))
                        nums[i] += mx
                for i in range(1, n):
                    if nums[i] < nums[i - 1]:
                        nums[i] += nums[i - 1]
                        ans.append((i + 1, i))
    # print(nums)
    print(len(ans))
    for i, j in ans:
        print(i, j)

for _ in range(int(input())):
    solve()
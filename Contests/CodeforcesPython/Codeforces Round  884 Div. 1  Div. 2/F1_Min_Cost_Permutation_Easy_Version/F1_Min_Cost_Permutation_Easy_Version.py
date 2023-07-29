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
    n, c = mint()
    nums = ints()
    if c >= 0:
        ans = sorted(nums)
    else:
        nums.sort(reverse = True)
        ans = []
        i = j = 0
        seen = [False] * n
        while i < n:
            if i >= n - 3:
                ans.extend(nums[i:])
                break
            if i >= j: j = i + 1
            while j < n - 1 and nums[j + 1] - nums[i + 1] >= c:
                j += 1

            ans.append(nums[i])
            if j > i + 2 and nums[i + 2] - nums[i] >= c:
                k = i + 2
                while k < j - 1:
                    while k < j - 1 and nums[k + 1] - ans[-1] >= c:
                        k += 1
                    ans.append(nums[k])
                    seen[k] = True
                    k += 1
                for k in range(j - 1, i, -1):
                    if seen[k]: continue
                    ans.append(nums[k])
                ans.append(nums[j])
                i = j + 1
            else:
                i += 1

    print(*ans)

for _ in range(int(input())):
    solve()
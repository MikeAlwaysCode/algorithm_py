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
    ans = []
    pre, i, j = 0, 0, n - 1
    while i <= j:
        if nums[i] > pre and nums[j] > pre:
            if nums[i] < nums[j]:
                ans.append("L")
                pre = nums[i]
                i += 1
            elif nums[i] > nums[j]:
                ans.append("R")
                pre = nums[j]
                j -= 1
            else:
                l = i
                while l < j and nums[l + 1] > nums[l]:
                    l += 1
                r = j
                while r > i and nums[r - 1] > nums[r]:
                    r -= 1
                if l - i > j - r:
                    ans.extend(["L"] * (l - i + 1))
                else:
                    ans.extend(["R"] * (j - r + 1))
                break
        elif nums[i] > pre:
            ans.append("L")
            pre = nums[i]
            i += 1
        elif nums[j] > pre:
            ans.append("R")
            pre = nums[j]
            j -= 1
        else:
            break

    print(len(ans))
    print("".join(ans))

solve()

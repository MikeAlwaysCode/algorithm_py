import sys
from collections import *
# from string import *

# import math
# import os
# import random
# from bisect import bisect, bisect_left
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from itertools import *
# from io import BytesIO, IOBase

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

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    s = sorted(Counter(input()).items(), reverse = True)
    m = sint()
    nums = ints()

    ans = [''] * m
    i = 0
    pos = [j for j, v in enumerate(nums) if v == 0]
    while True:
        while s[i][1] < len(pos):
            i += 1
        for j in pos:
            ans[j] = s[i][0]
        i += 1
        nxt = []
        for j, v in enumerate(nums):
            if v == 0:
                nums[j] = -1
                continue
            if v < 0:
                continue
            for k in pos:
                nums[j] -= abs(j - k)
            if nums[j] == 0:
                nxt.append(j)
        if not nxt: break
        pos = nxt
        
    print("".join(ans))

for _ in range(int(input())):
    solve()
import sys
import itertools

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

    pos = list(i for i in range(n) if nums[i] > 1)
    
    if not pos:
        print(1, 1)
        return
    
    pres = list(itertools.accumulate(nums, initial = 0))
    s = 1
    for i in pos:
        s *= nums[i]
        # if s >= pres[-1]:
        if s >= 1e10:
            print(pos[0] + 1, pos[-1] + 1)
            return
    
    mx = 0
    l = r = 1
    for i in range(len(pos)):
        s = 1
        for j in range(i, -1, -1):
            s *= nums[pos[j]]
            if s - pres[pos[i] + 1] + pres[pos[j]] > mx:
                mx = s - pres[pos[i] + 1] + pres[pos[j]]
                l, r = pos[j] + 1, pos[i] + 1

    print(l, r)

for _ in range(int(input())):
    solve()
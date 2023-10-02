import sys
import random
from collections import *

# import itertools
# import math
# import os
# from bisect import bisect, bisect_left
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
    h = random.randint(1, 1 << 30)
    cnt = Counter(x ^ h for x in nums)
    mex = 0
    while cnt[mex^h]:
        mex += 1
    
    if mex == 0:
        print(0)
        return
    # print(mex)
    dp = [0] * mex
    c0 = cnt[h]
    dp[0] = (c0 - 1) * mex
    for i in range(1, mex):
        v = cnt[i^h]
        dp[i] = mex * (v - 1) + i * c0
        for j in range(1, i):
            dp[i] = min(dp[i], dp[j] + mex * (v - 1) + i * cnt[j ^ h] - mex * (cnt[j ^ h] - 1))
    # print(dp)
    print(min(dp))

for _ in range(int(input())):
    solve()
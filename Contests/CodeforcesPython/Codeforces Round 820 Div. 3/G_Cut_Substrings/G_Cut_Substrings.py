from bisect import bisect, bisect_left
import sys

# import itertools
# import math
# import os
# import random
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
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    s = input()
    t = input()
    n, m = len(s), len(t)
    if m > n:
        print(0, 1)
        return

    pos = []
    for i in range(n - m + 1):
        if s[i:i + m] == t:
            pos.append(i)
    
    if not pos:
        print(0, 1)
        return
    
    n = len(pos)
    mn = i = 0
    while i < n:
        # 先找到范围内最后一个匹配t的位置
        j = bisect_left(pos, pos[i] + m) - 1
        # i跳到下一个必须处理的位置
        i = bisect_left(pos, pos[j] + m)
        mn += 1

    dp = [0] * (n + 1)
    dp[n] = 1

    for _ in range(mn):
        for i, x in enumerate(pos):
            res = 0
            j = bisect_left(pos, x + m)
            # i, j 范围内都可以作为一种选择
            for k in range(i, j):
                # 如果选择k，则从pos[k] + m转移而来
                res = (res + dp[bisect_left(pos, pos[k] + m)]) % MOD
            dp[i] = res

    print(mn, dp[0])

for _ in range(int(input())):
    solve()

import math
import sys

# import itertools
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
    n, k = mint()
    s = list(map(int, list(input())))
    max0pref = [[0] * (n + 1) for _ in range(n + 1)]
    max0suff = [[0] * (n + 1) for _ in range(n + 1)]
    for l in range(n):
        cnt1 = 0
        for r in range(l + 1, n + 1):
            cnt1 += int(s[r - 1] == 1)
            max0pref[r][cnt1] = max(max0pref[r][cnt1], r - l)
            max0suff[l][cnt1] = max(max0suff[l][cnt1], r - l)
    
    for r in range(n + 1):
        for cnt in range(n + 1):
            if r:
                max0pref[r][cnt] = max(max0pref[r][cnt], max0pref[r - 1][cnt])
            if cnt:
                max0pref[r][cnt] = max(max0pref[r][cnt], max0pref[r][cnt - 1])
    
    for l in range(n, -1, -1):
        for cnt in range(n + 1):
            if l + 1 <= n:
                max0suff[l][cnt] = max(max0suff[l][cnt], max0suff[l + 1][cnt])
            if cnt:
                max0suff[l][cnt] = max(max0suff[l][cnt], max0suff[l][cnt - 1])
    
    max0by1 = [-math.inf] * (n + 1)
    ans = [0] * (n + 1)
    for l in range(n):
        cnt0 = 0
        for r in range(l, n + 1):
            if r > l: cnt0 += int(s[r - 1] == 0)
            if cnt0 > k: break

            max0by1[r - l] = max(max0by1[r - l], max0pref[l][k - cnt0]);
            max0by1[r - l] = max(max0by1[r - l], max0suff[r][k - cnt0]);

    for i in range(n + 1):
        for a in range(1, n + 1):
            ans[a] = max(ans[a], i + max0by1[i] * a)
    
    print(*ans[1:])

for _ in range(int(input())):
    solve()
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
    n, m = map(int, input().split())
    s = input()
    
    pre = [0] * (n + 1)
    pre_mx = [0] * (n + 1)
    pre_mn = [0] * (n + 1)
    for i, c in enumerate(s):
        if c == "+":
            pre[i + 1] = pre[i] + 1
        else:
            pre[i + 1] = pre[i] - 1
        pre_mx[i + 1] = max(pre_mx[i], pre[i + 1])
        pre_mn[i + 1] = min(pre_mn[i], pre[i + 1])
    
    suf_mx = [0] * (n + 1)
    suf_mn = [0] * (n + 1)
    mx = mn = pre[-1]
    for i in range(n - 1, -1, -1):
        mx = max(mx, pre[i])
        mn = min(mn, pre[i])
        suf_mx[i] = max(suf_mx[i], mx - pre[i])
        suf_mn[i] = min(suf_mn[i], mn - pre[i])
    
    for _ in range(m):
        l, r = map(int, input().split())
        cmx = max(pre_mx[l - 1], pre[l - 1] + suf_mx[r])
        cmn = min(pre_mn[l - 1], pre[l - 1] + suf_mn[r])
        print(cmx - cmn + 1)

for _ in range(int(input())):
    solve()
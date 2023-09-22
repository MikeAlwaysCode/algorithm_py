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
    cost = ints()
    k = sint()
    d = [0] * (n + 1)
    ans = [0] * n
    stk = []
    for i, c in enumerate(cost):
        while stk and stk[-1][0] >= c:
            stk.pop()
        stk.append((c, i))
    m, k = divmod(k, stk[0][0])
    d[0] += m
    d[stk[0][1] + 1] -= m
    for i in range(1, len(stk)):
        c, j = stk[i]
        if m > 0 and k + stk[i - 1][0] >= c:
            m = min(m, k // (c - stk[i - 1][0]))
            k -= m * (c - stk[i - 1][0])
            d[stk[i - 1][1] + 1] += m
            d[j + 1] -= m
        else:
            break

    cnt = 0
    for i in range(n):
        cnt += d[i]
        ans[i] = cnt
    print(*ans)

for _ in range(int(input())):
    solve()
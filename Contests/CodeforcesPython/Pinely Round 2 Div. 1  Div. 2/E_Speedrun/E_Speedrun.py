import math
import sys
from collections import *

# import itertools
# import os
# import random
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
    n, m, k = mint()
    h = ints()
    l = h[:]
    r = h[:]
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(m):
        u, v = mint()
        u -= 1
        v -= 1
        deg[v] += 1
        g[u].append(v)

    q = deque((i for i in range(n) if deg[i] == 0))
    for i in range(n):
        u = q[i]
        for v in g[u]:
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)

    # 求出以i作为起点，最长的链
    dp = [0] * n
    for i in range(n - 1, -1, -1):
        u = q[i]
        for v in g[u]:
            dp[u] = max(dp[u], dp[v] + (h[v] - h[u]) % k)

    idx = sorted(range(n), key = lambda x: h[x])
    mx = 0
    for i in range(n):
        dp[i] += h[i]
        mx = max(mx, dp[i])
    ans = math.inf
    for i in idx:
        ans = min(ans, mx - h[i])
        mx = max(mx, dp[i] + k)
    print(ans)

for _ in range(int(input())):
    solve()
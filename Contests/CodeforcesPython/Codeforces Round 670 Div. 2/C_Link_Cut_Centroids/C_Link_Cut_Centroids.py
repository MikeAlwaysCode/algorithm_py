import sys
from collections import deque

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
    g = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = mint()
        deg[u] += 1
        deg[v] += 1
        g[u].append(v)
        g[v].append(u)
    
    x, y, z = 1, g[1][0], g[1][0]
    if not n & 1:
        cnt = [1] * (n + 1)
        parent = [-1] * (n + 1)
        q = deque(i for i in range(2, n + 1) if deg[i] == 1)
        while q:
            u = q.popleft()
            for v in g[u]:
                if v == 1:
                    cnt[v] += cnt[u]
                    parent[u] = 1
                elif deg[v] > 1:
                    deg[v] -= 1
                    cnt[v] += cnt[u]
                    parent[u] = v
                    if deg[v] == 1: q.append(v)
        for i in range(1, n + 1):
            if cnt[i] * 2 == n:
                z, y = i, parent[i]
                for v in g[y]:
                    if v != z:
                        x = v
                        break
                break

    print(x, y)
    print(x, z)

for _ in range(int(input())):
    solve()
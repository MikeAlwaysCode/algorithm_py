import sys
from collections import *

# import itertools
# import math
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
    n = sint()
    vals = ints()
    # deg = [0] * n
    # deg[0] += 1
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        # deg[u] += 1
        # deg[v] += 1
        g[u].append(v)
        g[v].append(u)
    
    ans = [0] * n
    cnt = [1] * n
    
    # 623 ms
    s = []
    parent = [-1] * n
    q = deque([(0, -1)])
    while q:
        x, p = q.popleft()
        for y in g[x]:
            if y == p: continue
            parent[y] = x
            s.append(y)
            q.append((y, x))
    
    for x in s[::-1]:
        ans[0] += (vals[x] ^ vals[parent[x]]) * cnt[x]
        cnt[parent[x]] += cnt[x]
    
    for x in s:
        ans[x] = ans[parent[x]] + (vals[x] ^ vals[parent[x]]) * (n - cnt[x] * 2)

    # # 779 ms
    # q = deque(i for i in range(n) if deg[i] == 1)
    # while q:
    #     x = q.popleft()
    #     for y in g[x]:
    #         if deg[y] == 1: continue
    #         ans[0] += (vals[x] ^ vals[y]) * cnt[x]
    #         cnt[y] += cnt[x]
    #         deg[y] -= 1
    #         if deg[y] == 1: q.append(y)
    
    # q = deque([(0, -1)])
    # while q:
    #     x, p = q.popleft()
    #     for y in g[x]:
    #         if y == p: continue
    #         ans[y] = ans[x] + (vals[x] ^ vals[y]) * (n - cnt[y] * 2)
    #         q.append((y, x))

    # # 1419 ms
    # @bootstrap
    # def dfs1(x: int, p: int):
    #     for y in g[x]:
    #         if y == p: continue
    #         yield dfs1(y, x)
    #         cnt[x] += cnt[y]
    #         ans[0] += (vals[x] ^ vals[y]) * cnt[y]
    #     yield
    
    # dfs1(0, -1)

    # @bootstrap
    # def dfs2(x: int, p: int):
    #     for y in g[x]:
    #         if y == p: continue
    #         ans[y] = ans[x] + (vals[x] ^ vals[y]) * (n - cnt[y] * 2)
    #         yield dfs2(y, x)
    #     yield
    
    # dfs2(0, -1)

    print(*ans)

for _ in range(int(input())):
    solve()
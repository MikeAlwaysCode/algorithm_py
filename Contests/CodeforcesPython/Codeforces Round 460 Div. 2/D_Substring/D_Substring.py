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
    n, m = mint()
    s = list(map(ord, input()))
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(m):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        deg[v] += 1
    # print(s)
    cnt = [[0] * 26 for _ in range(n)]
    ans = 0
    q = deque((i for i in range(n) if deg[i] == 0))
    path = 0
    while q:
        path += 1
        
        x = q.popleft()
        cnt[x][s[x] - 97] += 1
        for d in range(26):
            ans = max(ans, cnt[x][d])
        
        for y in g[x]:
            for d in range(26):
                cnt[y][d] = max(cnt[y][d], cnt[x][d])
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)
    if path != n:
        print(-1)
    else:
        print(ans)

solve()
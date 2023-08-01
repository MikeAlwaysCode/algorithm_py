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
    n, m = mint()
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = mint()
        g[u].append(v)
        g[v].append(u)
    cnt = [0] * 2
    col = [-1] * (n + 1)
    col[1] = 0
    q = deque([1])
    while q:
        x = q.popleft()
        cnt[col[x]] += 1
        for y in g[x]:
            if col[y] != -1: continue
            col[y] = col[x] ^ 1
            q.append(y)
    t = 0 if cnt[0] <= cnt[1] else 1
    ans = [i for i in range(1, n + 1) if col[i] == t]
    print(len(ans))
    print(*ans)

for _ in range(int(input())):
    solve()
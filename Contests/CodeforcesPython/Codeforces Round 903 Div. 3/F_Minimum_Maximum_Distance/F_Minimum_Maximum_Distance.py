import sys
from collections import *

# import math
# import os
# import random
# from bisect import bisect, bisect_left
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from itertools import *
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

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, k = mint()
    mark = set(x - 1 for x in ints())

    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    d1 = [0] * n
    d2 = [0] * n
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
        mx = d1[x]
        if mx:
            mx += 1
        elif x in mark:
            mx = 1
        p = parent[x]
        if d1[p] < mx:
            d1[p], d2[p] = mx, d1[p]
        elif d2[p] < mx:
            d2[p] = mx
    # print(d1)
    # print(d2)
    ans = [0] * n
    q = deque([(0, -1, -1)])
    while q:
        x, p, d = q.popleft()
        ans[x] = d1[x]
        if d == 0:
            if p in mark:
                d = 1
        else:
            d += 1
        ans[x] = max(ans[x], d)
        for y in g[x]:
            if y == p: continue
            mx = d1[y]
            if mx:
                mx += 1
            elif y in mark:
                mx = 1
            if mx == d1[x]:
                xd = d2[x]
            else:
                xd = d1[x]
            xd = max(xd, d)
            q.append((y, x, xd))
    # print(ans)
    print(min(ans))


for _ in range(int(input())):
    solve()
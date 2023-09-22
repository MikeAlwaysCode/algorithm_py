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
    n, a, b = mint()
    a -= 1
    b -= 1
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(n):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1
    
    if a == b:
        print("NO")
        return
    
    circle = [True] * n
    q = deque(i for i in range(n) if deg[i] == 1)
    while q:
        u = q.popleft()
        circle[u] = False
        for v in g[u]:
            if deg[v] == 1: continue
            deg[v] -= 1
            if deg[v] == 1:
                q.append(v)
    
    if circle[b]:
        print("YES")
        return

    d = [-1] * n
    q = [b]
    p = -1
    while q:
        tmp = q
        q = []
        p += 1
        for u in tmp:
            d[u] = p
            if circle[u]: continue
            for v in g[u]:
                if d[v] >= 0: continue
                q.append(v)
    
    c = [False] * n
    q = [a]
    p = -1
    c[a] = True
    while q:
        tmp = q
        q = []
        p += 1
        for u in tmp:
            if p <= d[u] and circle[u]:
                print("NO")
                return
            for v in g[u]:
                if c[v]: continue
                c[v] = True
                q.append(v)
        
    print("YES")

for _ in range(int(input())):
    solve()
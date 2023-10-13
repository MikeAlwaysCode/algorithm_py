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
    n = sint()
    deg = [0] * n
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        deg[u] += 1
        deg[v] += 1
        g[u].append(v)
        g[v].append(u)
        
    dis = [0] * n
    mn, mx = 0, n - 1
    
    q = deque([(0, -1)])
    while q:
        x, p = q.popleft()
        for y in g[x]:
            if y == p: continue
            dis[y] = dis[x] + 1
            q.append((y, x))
            if deg[x] == 1: deg[y] = 0
            if deg[y] == 1: deg[x] = 0
        if deg[x] == 1: # leaf
            mn |= 1 << (dis[x] & 1)
            mx -= 1
    
    if mn < 3: mn = 1
    mx += deg.count(0)
    
    print(mn, mx)


solve()
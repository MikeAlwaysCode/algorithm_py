import math
import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from random import *
from string import *
from types import GeneratorType

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
    n, m, l, s, t = mint()
    vis = [False] * m
    edges = []
    g = [[] for _ in range(n)]
    for i in range(m):
        u, v, w = mint()
        if w == 0:
            vis[i] = True
            w = 1
        edges.append([u, v, w])
        g[u].append((v, i))
        g[v].append((u, i))
    
    dis1 = [math.inf] * (n)
    dis1[s] = 0
    h = [(0, s)]
    while h:
        d, u = heappop(h)
        if d > dis1[u]: continue
        for v, i in g[u]:
            new_d = d + edges[i][2]
            if new_d < dis1[v]:
                dis1[v] = new_d
                heappush(h, (dis1[v], v))
    
    if dis1[t] > l:
        print("NO")
        return
    
    dis2 = [math.inf] * n
    dis2[s] = 0
    h = [(0, s)]
    while h:
        d, u = heappop(h)
        if d > dis2[u]: continue
        for v, i in g[u]:
            if vis[i] and edges[i][2] == 1 and edges[i][2] + d + dis1[t] - dis1[v] < l:
                x = l - edges[i][2] - d - dis1[t] + dis1[v]
                edges[i][2] += x
            new_d = d + edges[i][2]
            if new_d < dis2[v]:
                dis2[v] = new_d
                heappush(h, (dis2[v], v))

    if dis2[t] == l:
        print("YES")
        for e in edges:
            print(*e)
    else:
        print("NO")

# for _ in range(int(input())):
solve()
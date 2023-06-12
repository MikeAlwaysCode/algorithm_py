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
    n, m, k = mint()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    dis = [0] * n
    h = []
    for _ in range(k):
        u, d = mint()
        u -= 1
        dis[u] = d + 1
        h.append((-dis[u], u))

    heapify(h)
    while h:
        d, u = heappop(h)
        d = -d
        if d < dis[u]: continue
        d -= 1
        for v in g[u]:
            if d <= dis[v]: continue
            dis[v] = d
            if d > 1: heappush(h, (-d, v))
    
    ans = [i + 1 for i in range(n) if dis[i]]
    print(len(ans))
    print(*ans)

solve()
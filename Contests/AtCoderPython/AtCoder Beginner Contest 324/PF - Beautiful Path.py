import sys
from heapq import *

# import math
# from bisect import *
# from collections import *
# from functools import *
# from itertools import *
# from random import *
# from string import *
# from types import GeneratorType

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
'''
class MaxItem:
    def __init__(self, x: int, beauty: int, cost: int) -> None:
        self.x = x
        self.beauty = beauty
        self.cost = cost
    def __lt__(self, o):
        return self.beauty * o.cost > self.cost * o.beauty
    def getResult(self):
        return self.beauty / self.cost

def solve() -> None:
    n, m = mint()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, b, c = mint()
        u -= 1
        v -= 1
        g[u].append((v, b, c))
    
    dis = [MaxItem(i, 0, 0) for i in range(n)]
    h = [(dis[0], dis[0].beauty, dis[0].cost)]
    while h:
        u, ub, uc = heappop(h)
        if u.beauty != ub or u.cost != uc:
            continue
        for v, vb, vc in g[u.x]:
            if dis[v].beauty == 0 or (ub + vb) * dis[v].cost > (uc + vc) * dis[v].beauty:
                dis[v].beauty, dis[v].cost = ub + vb, uc + vc
                heappush(h, (dis[v], dis[v].beauty, dis[v].cost))

    print(dis[-1].getResult())
'''
def solve() -> None:
    n, m = mint()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, b, c = mint()
        u -= 1
        v -= 1
        g[u].append((v, b, c))
    
    dis = [[0, 0, 0] for _ in range(n)]
    h = [(0, 0)]
    while h:
        p, u = heappop(h)
        p = -p
        if p + 0.0001 < dis[u][2]:
            continue
        for v, b, c in g[u]:
            if dis[v][0] == 0 or (dis[u][0] + b) * dis[v][1] > (dis[u][1] + c) * dis[v][0]:
                dis[v][0], dis[v][1] = dis[u][0] + b, dis[u][1] + c
                dis[v][2] = dis[v][0] / dis[v][1]
                heappush(h, (-dis[v][2], v))

    print(dis[-1][2])

solve()
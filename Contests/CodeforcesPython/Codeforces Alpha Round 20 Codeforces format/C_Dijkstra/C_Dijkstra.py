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
    n, m = mint()
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = mint()
        g[u].append((v, w))
        g[v].append((u, w))
    
    dis = [math.inf] * (n + 1)
    nxt = [-1] * (n + 1)
    dis[n] = 0
    q = [(0 , n )]
    while q:
        d, u = heappop(q)
        if d > dis[u]: continue
        for v, w in g[u]:
            if d + w > dis[v]: continue
            nxt[v] = u
            dis[v] = d + w
            heappush(q, (dis[v], v))
            
    if dis[1] == math.inf:
        print(-1)
    else:
        ans = [1]
        while ans[-1] != n:
            ans.append(nxt[ans[-1]])
        print(*ans)
        
    '''
    dis = [math.inf] * (n + 1)
    dis[n] = 0
    q = [(0 , n )]
    while q:
        d, u = heappop(q)
        if d > dis[u]: continue
        for v, w in g[u]:
            if d + w > dis[v]: continue
            dis[v] = d + w
            heappush(q, (dis[v], v))
            
    if dis[1] == math.inf:
        print(-1)
    else:
        ans = [1]
        while ans[-1] != n:
            for u, w in g[ans[-1]]:
                if dis[u] + w == dis[ans[-1]]:
                    ans.append(u)
                    break
        print(*ans)
    '''

# for _ in range(int(input())):
solve()
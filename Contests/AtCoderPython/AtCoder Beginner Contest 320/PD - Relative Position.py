import sys
from collections import *

# import math
# from bisect import *
# from functools import *
# from heapq import *
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

def solve() -> None:
    n, m = mint()
    pos = [None] * n
    pos[0] = (0, 0)
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, x, y = mint()
        u -= 1
        v -= 1
        g[u].append((v, x, y))
        g[v].append((u, -x, -y))
    
    q = deque([0])
    
    while q:
        u = q.popleft()
        ux, uy = pos[u]
        for v, x, y in g[u]:
            if pos[v] is not None: continue
            pos[v] = (ux + x, uy + y)
            q.append(v)
    
    for p in pos:
        if p is None:
            print("undecidable")
        else:
            print(p[0], p[1])

solve()
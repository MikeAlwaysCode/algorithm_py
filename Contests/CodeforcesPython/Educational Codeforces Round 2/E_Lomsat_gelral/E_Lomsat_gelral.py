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
    n = sint()
    c = ints()
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        deg[u] += 1
        deg[v] += 1
        g[u].append(v)
        g[v].append(u)
    deg[0] += 1
    cnt = [Counter([x]) for x in c]
    mx = [1] * n
    ans = c
    q = deque(i for i in range(n) if deg[i] == 1)
    while q:
        u = q.popleft()
        for v in g[u]:
            if deg[v] <= 1: continue

            if len(cnt[u]) > len(cnt[v]):
                cnt[u], cnt[v] = cnt[v], cnt[u]
                mx[v] = mx[u]
                ans[v] = ans[u]
            
            for k in cnt[u].keys():
                cnt[v][k] += cnt[u][k]
                if cnt[v][k] > mx[v]:
                    mx[v] = cnt[v][k]
                    ans[v] = k
                elif cnt[v][k] == mx[v]:
                    ans[v] += k

            deg[v] -= 1
            if deg[v] == 1:
                q.append(v)
            break

    print(*ans)

solve()

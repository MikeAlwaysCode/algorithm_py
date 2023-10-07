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
    g = [[] for _ in range(n)]
    deg = [0] * n
    time = [1] * n
    q = deque()
    ans = cnt = 0
    for i in range(n):
        req = ints()
        if req[0] == 0:
            q.append(i)
        else:
            deg[i] = req[0]
            for j in req[1:]:
                g[j - 1].append(i)

    while q:
        u = q.popleft()
        cnt += 1
        ans = max(ans, time[u])
        for v in g[u]:
            if v > u:
                time[v] = max(time[v], time[u])
            else:
                time[v] = max(time[v], time[u] + 1)
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    
    print(ans if cnt == n else -1)

for _ in range(int(input())):
    solve()
import sys
from collections import deque

# import itertools
# import math
# import os
# import random
# from bisect import bisect, bisect_left
# from collections import *
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
DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, m = mint()
    cnt = 0
    g = []

    for _ in range(n):
        g.append(list(input()))
        cnt += g[-1].count("#")
    
    if cnt < 3:
        print(-1)
        return
    
    seen = [[0] * m for _ in range(n)]
    t = 0
    
    def bfs(x: int, y: int) -> int:
        q = deque([(x, y)])
        res = 1
        seen[x][y] = t
        while q:
            x, y = q.popleft()
            for d in DIR:
                nx, ny = x + d[0], y + d[1]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or seen[nx][ny] == t or g[nx][ny] == ".": continue
                res += 1
                seen[nx][ny] = t
                q.append((nx, ny))
        return res
    
    for i in range(n):
        for j in range(m):
            if g[i][j] == ".": continue
            connected = x = y = 0
            for d in DIR:
                nx, ny = i + d[0], j + d[1]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or g[nx][ny] == ".": continue
                connected += 1
                x, y = nx, ny
            if connected < 2: continue
            g[i][j] = "."
            t += 1
            ncnt = bfs(x, y)
            if ncnt < cnt - 1:
                print(1)
                return
            g[i][j] = "#"

    print(2)

solve()
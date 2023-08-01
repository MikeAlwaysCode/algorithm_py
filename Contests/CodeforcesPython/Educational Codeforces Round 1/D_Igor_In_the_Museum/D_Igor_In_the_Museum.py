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
    n, m, k = mint()

    fa = list(range(n * m))
    def find(x: int):
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            fa[cur], cur = x, fa[cur]
        return x
    def union(x: int, y: int) -> bool:
        x, y = find(x), find(y)
        if x == y: return False
        fa[y] = x
        return True
    
    cnt = [0] * (n * m)

    g = []
    for _ in range(n):
        g.append(input())
    
    for i in range(n):
        for j in range(m):
            if g[i][j] != '.': continue
            x = find(i * m + j)
            if cnt[x]: continue
            q = deque([(i, j)])
            while q:
                r, c = q.popleft()
                cur = 0
                for dr, dc in DIR:
                    nr, nc = r + dr, c + dc
                    if g[nr][nc] != '.':
                        cur += 1
                        continue
                    y = find(nr * m + nc)
                    if y == x: continue
                    union(x, y)
                    q.append((nr, nc))
                cnt[x] += cur
    
    for _ in range(k):
        x, y = mint()
        print(cnt[find((x - 1) * m + y - 1)])

solve()
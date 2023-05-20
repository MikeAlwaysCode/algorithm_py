import sys
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from math import *
from random import *
from string import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, m = map(int, input().split())
    g = []
    for _ in range(n):
        g.append(ints())

    ans = 0

    def bfs(i: int, j: int) -> int:
        q = deque([(i, j)])
        res = g[i][j]
        g[i][j] = 0
        while q:
            r, c = q.popleft()
            for x, y in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if x < 0 or x >= n or y < 0 or y >= m or g[x][y] == 0: continue
                res += g[x][y]
                g[x][y] = 0
                q.append((x, y))
        return res

    for i in range(n):
        for j in range(m):
            if g[i][j] == 0: continue
            ans = max(ans, bfs(i, j))
    print(ans)

for _ in range(int(input())):
    solve()

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
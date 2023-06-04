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
DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, m = mint()
    g = []
    good, bad = [], []
    for i in range(n):
        g.append(list(input()))
        for j in range(m):
            if g[-1][j] == 'G':
                good.append((i, j))
            elif g[-1][j] == 'B':
                bad.append((i, j))

    if not good:
        print("Yes")
        return
    
    # 把Bad四周Ban掉，如果跟Good相连，则必然无解
    for x, y in bad:
        for dr, dc in DIR:
            nx, ny = x + dr, y + dc
            if nx < 0 or nx >= n or ny < 0 or ny >= m or g[nx][ny] == "#" or g[nx][ny] == "B": continue
            if g[nx][ny] == "G":
                print("No")
                return
            g[nx][ny] = "#"
    
    # 若终点被Ban
    if g[n - 1][m - 1] != ".":
        print("No")
        return
    
    visited = [[False] * m for _ in range(n)]
    visited[n - 1][m - 1] = True
    q = deque([(n - 1, m - 1)])
    while q:
        x, y = q.popleft()
        for dr, dc in DIR:
            nx, ny = x + dr, y + dc
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or g[nx][ny] == "#": continue
            visited[nx][ny] = True
            q.append((nx, ny))
    
    for x, y in good:
        # 若有Good无法抵达
        if not visited[x][y]:
            print("No")
            return

    print("Yes")

for _ in range(int(input())):
    solve()
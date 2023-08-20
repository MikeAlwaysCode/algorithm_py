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
    h, w, t = mint()
    mat = []
    sx = sy = gx = gy = -1
    p = []
    
    for i in range(h):
        mat.append(list(input()))
        for j, c in enumerate(mat[-1]):
            if c == "S":
                sx, sy = i, j
            elif c == "G":
                gx, gy = i, j
            elif c == "o":
                p.append((i, j))
    
    p.insert(0, (sx, sy))
    
    # BFS求点出发到其他点的最短路
    def bfs(i: int, j: int) -> list:
        dis = [[math.inf] * w for _ in range(h)]
        dis[i][j] = 0
        q = deque([(i, j)])
        while q:
            x, y = q.popleft()
            for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if nx < 0 or nx >= h or ny < 0 or ny >= w or mat[nx][ny] == "#" or dis[nx][ny] <= dis[x][y] + 1:
                    continue
                dis[nx][ny] = dis[x][y] + 1
                q.append((nx, ny))
        return dis

    # 先求出所有点到终点的最短路
    last = bfs(gx, gy)
    if last[sx][sy] > t:
        print(-1)
        return
    
    m = len(p)
    # 求出起点及所有关键点之间的距离
    dis = [[0] * m for _ in range(m)]
    for i in range(m):
        d = bfs(p[i][0], p[i][1])
        for j in range(m):
            dis[i][j] = d[p[j][0]][p[j][1]]
    
    # traveling salesman
    ans = -1
    dp = [[math.inf] * m for _ in range(1 << m)]
    dp[1][0] = 0
    for s in range(1, 1 << m, 2):
        for i in range(m):
            if dp[s][i] == math.inf: continue
            if dp[s][i] + last[p[i][0]][p[i][1]] <= t:
                cnt = bin(s)[2:].count("1") - 1
                ans = max(ans, cnt)
            for j in range(m):
                if (s >> j) & 1 or dis[i][j] == math.inf: continue
                dp[s | (1 << j)][j] = min(dp[s | (1 << j)][j], dp[s][i] + dis[i][j])

    print(ans)

solve()
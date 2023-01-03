import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n, m, k = map(int, input().split())
    grid = []
    cnt = 0
    i = j = -1
    for _ in range(n):
        grid.append(list(input().strip()))
        cnt += grid[-1].count('.')
        if i == -1 and cnt > 0: # Start position
            i = len(grid) - 1
            j = grid[-1].index('.')
    
    dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    visited = [[False] * m for _ in range(n)]

    def dfs(x: int, y: int) -> None:
        nonlocal cnt
        if cnt <= k:
            grid[x][y] = 'X'
        cnt -= 1
        visited[x][y] = True
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.' and not visited[nx][ny]:
                dfs(nx, ny)
    
    # Python DFS 会爆Stack !!!!
    # dfs(i, j)
    # print(cnt)
    # BFS
    q = [(i, j)]
    visited[i][j] = True
    while q:
        tmp = q
        q = []
        for x, y in tmp:
            # print(x, y, cnt)
            if cnt <= k:
                grid[x][y] = 'X'
            cnt -= 1
            
            for dx, dy in dir:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    for row in grid:
        print("".join(row))

t = 1
for _ in range(t):
    solve()
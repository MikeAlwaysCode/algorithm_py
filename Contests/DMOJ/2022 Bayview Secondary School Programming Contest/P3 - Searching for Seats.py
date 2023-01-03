import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

DIR = ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1))

def solve() -> None:
    n, m, k = map(int, input().split())
    grid = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        grid[x][y] = -1
        
        for dr, dc in DIR:
            nx, ny = x + dr, y + dc
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != -1:
                grid[nx][ny] += 1

    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] >= 3:
                ans += 1

    print(ans)

# t = int(input())
# for _ in range(t):
solve()
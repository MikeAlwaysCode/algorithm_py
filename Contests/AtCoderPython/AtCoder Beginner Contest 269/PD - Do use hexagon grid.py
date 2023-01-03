import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    black = []
    grid = [[0] * 2003 for _ in range(2003)]
    SHIFT = 1000
    
    for _ in range(n):
        x, y = map(int, input().split())
        black.append((x, y))
        grid[x+SHIFT][y+SHIFT] = 1

    dir = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]

    ans = 0
    for p in black:
        x, y = p[0], p[1]
        if grid[x+SHIFT][y+SHIFT]:
            ans += 1
            q = []
            q.append((x, y))
            grid[x+SHIFT][y+SHIFT] = 0
            # bfs
            while q:
                tmp = q
                q = []
                for v in tmp:
                    for d in dir:
                        nx = v[0] + d[0]
                        ny = v[1] + d[1]
                        if grid[nx+SHIFT][ny+SHIFT]:
                            q.append((nx, ny))
                            grid[nx+SHIFT][ny+SHIFT] = 0

    print(ans)

# t = int(input())
# for _ in range(t):
solve()
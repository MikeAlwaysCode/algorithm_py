import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(ints())
    
    chk = [[0] * m for _ in range(n)]
    chk[n-1][m-1] = grid[n-1][m-1]

    DIR = ((-1, 0), (0, -1))
    TDIR = ((1, 0), (0, 1))
    q = collections.deque([(n - 1, m - 1)])
    while q:
        (x, y) = q.popleft()
        if (x + y - 2) & 1:
            Becky = True
        else:
            Becky = False
        for dr, dc in DIR:
            nx, ny = x + dr, y + dc
            if 0 <= nx and 0 <= ny and not chk[nx][ny]:
                valid = True
                mn, mx, mnx, mny = 10 ** 11, 0, -1, -1
                for tdr, tdc in TDIR:
                    tnx, tny = nx + tdr, ny + tdc
                    if 0 <= tnx < n and 0 <= tny < m and not chk[tnx][tny]:
                        valid = False
                        break
                    elif 0 <= tnx < n and 0 <= tny < m:
                        mn = min(mn, chk[tnx][tny])
                        if grid[tnx][tny] > mx:
                            mx = grid[tnx][tny]
                            mnx, mny = tnx, tny
                if not valid and not chk[nx][ny]:
                    continue
                q.append((nx, ny))
                if Becky:
                    chk[nx][ny] = max(mn, grid[nx][ny])
                else:
                    chk[nx][ny] = max(chk[mnx][mny], grid[nx][ny])
    # print(chk)
    print(chk[0][0])

t = int(input())
for _ in range(t):
    solve()
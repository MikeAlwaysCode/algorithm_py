import sys
from collections import deque

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n, m = mint()
    g = []
    for _ in range(n):
        g.append(input())
    mat = [[0] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == '#':
                mat[i][j] = -1
                for dr, dc in DIR:
                    ni, nj = i + dr, j + dc
                    if 0 <= ni < n and 0 <= nj < m and mat[ni][nj] == 0:
                        mat[ni][nj] = 1
            elif ans == 0:
                ans = 1
    
    t = 1
    for i in range(n):
        for j in range(m):
            if mat[i][j]:
                continue
            t += 1
            q = deque([(i, j)])
            res, mat[i][j] = 1, -1
            while q:
                x, y = q.popleft()
                for dr, dc in DIR:
                    nx, ny = x + dr, y + dc
                    if 0 <= nx < n and 0 <= ny < m:
                        if mat[nx][ny] == 0:
                            mat[nx][ny] = -1
                            res += 1
                            q.append((nx, ny))
                        elif mat[nx][ny] != -1 and mat[nx][ny] != t:
                            mat[nx][ny] = t
                            res += 1
            ans = max(ans, res)
    print(ans)


solve()

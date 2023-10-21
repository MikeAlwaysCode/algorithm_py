import sys
from collections import deque

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, m = mint()
    g = []
    for _ in range(n):
        g.append(input())
    
    seen = [[False] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if seen[i][j] or g[i][j] == '.': continue
            ans += 1
            q = deque([(i, j)])
            seen[i][j] = True
            while q:
                x, y = q.popleft()
                for dr, dc in DIR8:
                    nx, ny = x + dr, y + dc
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or g[nx][ny] == '.' or seen[nx][ny]: continue
                    seen[nx][ny] = True
                    q.append((nx, ny))
    print(ans)

solve()
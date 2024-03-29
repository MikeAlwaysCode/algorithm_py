import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n, m = mint()
    g = []
    for _ in range(n):
        g.append(list(input()))
    
    if g[0][0] != g[-1][-1]:
        print(0)
        return

    dp = [[0] * (n + 2) for _ in range(n + 1)]
    dp[1][n] = 1
    for i in range(1, (n + m - 2) // 2 + 1):    # step: i
        for r1 in range(min(n, i + 1), max(0, i - m + 1), -1):
            c1 = i + 2 - r1
            for r2 in range(max(1, n - i), min(n + 1, n - i + m)):
                c2 = m - i + n - r2
                if g[r1 - 1][c1 - 1] == g[r2 - 1][c2 - 1]:
                    dp[r1][r2] = (dp[r1][r2] + dp[r1][r2 + 1] + dp[r1 - 1][r2] + dp[r1 - 1][r2 + 1]) % MOD
                else:
                    dp[r1][r2] = 0
    
    if (n + m) & 1:
        ans = sum(dp[i][i] + dp[i][i + 1] for i in range(1, n + 1)) % MOD
    else:
        ans = sum(dp[i][i] for i in range(1, n + 1)) % MOD

    '''
    ans = 0

    q = deque([(0, 0, n - 1, m - 1)])
    while q:
        x1, y1, x2, y2 = q.popleft()
        for nx1, ny1 in (x1 + 1, y1), (x1, y1 + 1):
            for nx2, ny2 in (x2 - 1, y2), (x2, y2 - 1):
                if nx1 > nx2 or ny1 > ny2 or g[nx1][ny1] != g[nx2][ny2]: continue
                if (nx1 == nx2 and ny1 == ny2) or (nx1 == nx2 and ny1 + 1 == ny2) or (nx1 + 1 == nx2 and ny1 == ny2): ans = (ans + 1) % MOD
                else: q.append((nx1, ny1, nx2, ny2))
    '''

    print(ans)

solve()

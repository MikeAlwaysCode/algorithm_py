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
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n, m, k = mint()
    g = [list(int(c == '#') for c in input()) for _ in range(n)]
    
    k = min(k, n + m - 2)

    ans = 0
    for r in range(2):
        if r:
            for row in g:
                row.reverse()
        for _ in range(2):
            dia = deque([0] * (m + k))
            col = [0] * m

            for i in range(n):
                dia.pop()
                dia.appendleft(0)
                dp = [0] * m

                for j in range(m - 1, -1, -1):
                    dia[j] += g[i][j]
                    
                    if i > k and j < m - 1 and j + k + 1 >= m:
                        dia[j + k + 1] -= g[i - k - 1][j]

                    if i > k and j > k:
                        dia[j] -= g[i - k - 1][j - k - 1]

                    col[j] += g[i][j]
                    if i > k:
                        col[j] -= g[i - k - 1][j]

                    dp[j] = col[j]
                    if j < m - 1:
                        dp[j] += dp[j + 1]
                    if j + 1 < m:
                        dp[j] -= dia[j + k + 1]
                    ans = max(ans, dp[j])

            g.reverse()

    print(ans)

for _ in range(int(input())):
    solve()

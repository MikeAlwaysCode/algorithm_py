import math
import sys

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
    row, col = [], []
    for _ in range(n):
        row.append(ints())
    for _ in range(n - 1):
        col.append(ints())

    if k & 1:
        ans = [-1] * m
        for _ in range(n):
            print(*ans)
    else:
        dp = [[0] * m for _ in range(n)]
        for _ in range(k // 2):
            tmp = [[math.inf] * m for _ in range(n)]
            for i in range(n):
                # left & right
                for j in range(m):
                    if j < m - 1:
                        tmp[i][j + 1] = min(tmp[i][j + 1], dp[i][j] + row[i][j])
                        tmp[i][j] = min(tmp[i][j], dp[i][j + 1] + row[i][j])
                    if i < n - 1:
                        tmp[i + 1][j] = min(tmp[i + 1][j], dp[i][j] + col[i][j])
                        tmp[i][j] = min(tmp[i][j], dp[i + 1][j] + col[i][j])
            dp = tmp

        for s in dp:
            print(*[v * 2 for v in s])


solve()

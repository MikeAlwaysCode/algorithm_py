import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    inv2 = pow(2, MOD - 2, MOD)
    for i in range(2, n + 1):
        a, b = 1, 0
        for j in range(1, i + 1):
            b = (b + dp[i - 1][j - 1]) * inv2 % MOD
            a = a * inv2 % MOD
        dp[i][i] = b * pow((1 - a) % MOD, MOD - 2, MOD) % MOD
        dp[i][1] = dp[i][i] * inv2 % MOD
        for j in range(2, i):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i][j - 1]) * inv2 % MOD

    print(*dp[n][1:])


solve()

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
    n, m, k, d = mint()
    win = k * pow(n, MOD - 2, MOD) % MOD
    lose = (1 - win) % MOD

    '''
    # 1. Probability
    ans = 0
    dp = [0] * d
    dp[0] = 1
    for _ in range(m):
        tmp = dp[-1]
        ans = (ans + dp[-1] * lose) % MOD
        for i in range(d - 2, -1, -1):
            tmp = (tmp + dp[i] * win) % MOD
            dp[i + 1] = dp[i] * lose % MOD
        dp[0] = tmp
    print((ans * n + m * k) % MOD)
    '''

    # 2. Expectation
    dp = [0] * d
    for _ in range(m):
        tmp = (dp[0] + 1) % MOD
        for i in range(d - 1):
            dp[i] = (tmp * win % MOD + dp[i + 1] * lose % MOD) % MOD
        dp[-1] = tmp
    print(dp[0] * n % MOD)


for _ in range(sint()):
    solve()

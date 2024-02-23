import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    prob = list(map(float, input().split()))
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i, p in enumerate(prob):
        for j in range(i + 1):
            dp[j + 1][i - j] += dp[j][i - j] * p
            dp[j][i - j + 1] += dp[j][i - j] * (1 - p)
    ans = 0
    for i in range(n, n // 2, -1):
        ans += dp[i][n - i]
    print(ans)

solve()

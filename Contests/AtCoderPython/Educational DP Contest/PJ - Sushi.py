import sys
from collections import Counter
from functools import cache

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
    cnt = Counter(ints())

    dp = [[[0.0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(cnt[3] + 1):
        for j in range(cnt[2] + cnt[3] - i + 1):
            for k in range(n - i - j + 1):
                if i == j == k == 0:
                    continue
                dp[i][j][k] = n
                if i:
                    dp[i][j][k] += i * dp[i - 1][j + 1][k]
                if j:
                    dp[i][j][k] += j * dp[i][j - 1][k + 1]
                if k:
                    dp[i][j][k] += k * dp[i][j][k - 1]
                dp[i][j][k] /= (i + j + k)
    print(dp[cnt[3]][cnt[2]][cnt[1]])
    '''
    @cache
    def dfs(i: int, j: int, k: int) -> float:
        if i == j == k == 0:
            return 0
        res = n
        if i:
            res += i * dfs(i - 1, j, k)
        if j:
            res += j * dfs(i + 1, j - 1, k)
        if k:
            res += k * dfs(i, j + 1, k - 1)
        return res / (i + j + k)

    print(dfs(cnt[1], cnt[2], cnt[3]))
    '''

solve()

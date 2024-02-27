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
    n, l, d = mint()

    # Y获得的数字的概率
    p = [0.0] * (l + d + 1)
    for i in range(1,l + d + 1):
        if i > l:   # 至多从i - d 到 l - 1转移而来
            p[i] = p[l - 1] - p[max(i - d - 1, 0)]
        elif i - d >= 1:    # 从i - d到i - 1转移而来
            p[i] = p[i - 1] - p[i - d - 1]
        else:
            p[i] = p[i - 1]
        if i <= d:
            p[i] += 1
        p[i] = p[i] / d + p[i - 1]

    # 计算X获胜概率
    dp = [0.0] * (n + 1)
    s = 0
    for i in range(n, -1, -1):
        if i > l + d - 1:   # Y至多l + d - 1，则X必胜
            dp[i] = 1
        else:               # 若继续投掷，胜率是sum(dp[i + 1:i + d]) / d, 否则，Y投掷到大于等于i且小于等于n是必输的概率，赢则1-p
            dp[i] = max(s / d, 1 - p[min(n, l + d)] + p[max(i, l) - 1])
        s += dp[i]
        if i + d <= n:
            s -= dp[i + d]
    print(dp[0])

solve()

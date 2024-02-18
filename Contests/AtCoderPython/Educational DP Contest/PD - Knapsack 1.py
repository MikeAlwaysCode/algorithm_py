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
    n, w = mint()
    dp = [0] * (w + 1)
    for _ in range(n):
        a, v = mint()
        for i in range(w, a - 1, -1):
            dp[i] = max(dp[i], dp[i - a] + v)
    print(dp[-1])


solve()

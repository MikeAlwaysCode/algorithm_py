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
    s = input()
    t = input()
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    prev = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = dp[i][j + 1]
            prev[i + 1][j + 1] = 1

            if dp[i + 1][j] > dp[i + 1][j + 1]:
                dp[i + 1][j + 1] = dp[i + 1][j]
                prev[i + 1][j + 1] = 2

            if s[i] == t[j] and dp[i][j] + 1 > dp[i + 1][j + 1]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                prev[i + 1][j + 1] = 3

    ans = []
    i, j = n, m
    while dp[i][j]:
        if prev[i][j] == 3:
            ans.append(s[i - 1])
            i -= 1
            j -= 1
        elif prev[i][j] == 1:
            i -= 1
        else:
            j -= 1
    
    print("".join(reversed(ans)))

solve()

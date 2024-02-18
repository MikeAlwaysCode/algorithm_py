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
    n = sint()
    s = input()
    ans = 0
    dp = [0] * (n + 3)
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            dp[i] = dp[i + 3] + n - i
        else:
            dp[i] = dp[i + 1]
        ans += dp[i]
    print(ans)


for _ in range(int(input())):
    solve()

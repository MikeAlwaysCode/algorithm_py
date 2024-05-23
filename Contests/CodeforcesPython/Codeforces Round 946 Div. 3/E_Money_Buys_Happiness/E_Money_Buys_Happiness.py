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
    m, x = mint()
    mx = 0
    c = [0] * m
    h = [0] * m
    for i in range(m):
        c[i], h[i] = mint()
        mx += h[i]
    dp = [-1] * (mx + 1)
    dp[0] = 0
    for i in range(m):
        for j in range(mx, -1, -1):
            if dp[j] == -1:
                continue
            if dp[j] >= c[i]:
                dp[j + h[i]] = max(dp[j + h[i]], dp[j] + x - c[i])
            dp[j] = max(dp[j], dp[j] + x)
    ans = max(v for v, d in enumerate(dp) if d != -1)
    print(ans)


for _ in range(int(input())):
    solve()

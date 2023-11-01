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
    n, m = mint()
    g = []
    for _ in range(n):
        g.append(ints())
    
    up = list(range(n))
    dp = [1] * m
    for i in range(1, n):
        for j in range(m):
            if g[i][j] >= g[i - 1][j]:
                dp[j] += 1
            else:
                dp[j] = 1
            up[i] = min(up[i], i - dp[j] + 1)

    for _ in range(sint()):
        l, r = mint()
        print("Yes" if up[r - 1] <= l - 1 else "No")

solve()
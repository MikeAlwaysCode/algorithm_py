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
    ds, dw = [], []
    for _ in range(n):
        s, w = input().split()
        ds.append(s)
        dw.append(w)
    
    g = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if ds[i] == ds[j] or dw[i] == dw[j]:
                g[i][j] = g[j][i] = True
    
    dp = [[False] * n for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i][i] = True
    ans = 0
    for mask in range(1, 1 << n):
        for i in range(n):
            if not dp[mask][i]:
                continue
            ans = max(ans, bin(mask)[2:].count('1'))
            for j in range(n):
                if (mask >> j) & 1 or not g[i][j]:
                    continue
                dp[mask | (1 << j)][j] = True

    print(n - ans)

for _ in range(int(input())):
    solve()

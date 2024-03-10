import math
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
    p = []
    s = set()
    for _ in range(n):
        p.append(ints())
        for x in p[-1]:
            s.add(x)
    r = []
    for _ in range(n):
        r.append(ints())
    d = []
    for _ in range(n - 1):
        d.append(ints())
    
    s = sorted(s)
    mp = {v:i for i, v in enumerate(s)}
    m = len(mp)
    dp = [[None] * m for _ in range(n * n)]
    dp[0][mp[p[0][0]]] = (0, 0)
    ans = math.inf
    for i in range(n):
        for j in range(n):
            for k in range(m):
                if not dp[i * n + j][k]:
                    continue

                t, left = dp[i * n + j][k]
                if i == n - 1 and j == n - 1:
                    ans = min(ans, t)
                    continue

                pw = s[k]
                
                if j < n - 1:
                    npi = max(k, mp[p[i][j + 1]])
                    nt, nleft = t, left - r[i][j]
                    if nleft < 0:
                        nt += (-nleft + pw - 1) // pw
                        nleft += (nt - t) * pw
                    if not dp[i * n + j + 1][npi] or (nt < dp[i * n + j + 1][npi][0]) or (nt == dp[i * n + j + 1][npi][0] and nleft > dp[i * n + j + 1][npi][1]):
                        dp[i * n + j + 1][npi] = (nt, nleft)

                if i < n - 1:
                    npi = max(k, mp[p[i + 1][j]])
                    nt, nleft = t, left - d[i][j]
                    if nleft < 0:
                        nt += (-nleft + pw - 1) // pw
                        nleft += (nt - t) * pw
                    if not dp[(i + 1) * n + j][npi] or (nt < dp[(i + 1) * n + j][npi][0]) or (nt == dp[(i + 1) * n + j][npi][0] and nleft > dp[(i + 1) * n + j][npi][1]):
                        dp[(i + 1) * n + j][npi] = (nt, nleft)
    
    print(ans + (n - 1) * 2)

solve()

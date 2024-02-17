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
    n, m = mint()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    w = ints()
    a = ints()
    
    s = [set() for _ in range(n)]

    idx = sorted(range(n), key = lambda x: w[x])
    sz = [0] * n
    for u in idx:
        dp = [0] * w[u]
        dp[0] = 1
        for v in g[u]:
            if w[v] >= w[u]:
                continue
            for j in range(w[u] - 1, w[v] - 1, -1):
                dp[j] = max(dp[j], dp[j - w[v]] + sz[v])
        sz[u] = max(dp)
    ans = sum(a[i] * sz[i] for i in range(n))
    # idx.sort(key = lambda x: -w[x])
    # ans = 0
    # for u in idx:
    #     ans += a[u]
    #     for v in s[u]:
    #         a[v] += a[u]
    print(ans)


solve()

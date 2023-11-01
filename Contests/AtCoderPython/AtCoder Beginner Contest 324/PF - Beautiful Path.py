import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# print = lambda d: sys.stdout.write(str(d) + "\n")
# endregion fastio

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, m = mint()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, b, c = mint()
        u -= 1
        v -= 1
        g[u].append((v, b, c))

    '''
    # 3407 ms
    def check(m):
        dp = [-1e8] * n
        dp[0] = 0.0
        for u in range(n):
            for v, b, c in g[u]:
                dp[v] = max(dp[v], dp[u] + b - c * m)
        return dp[-1] >= 0.0
    '''

    # 821 ms
    edges = []
    seen = [False] * n
    seen[0] = True
    for u in range(n):
        if seen[u]:
            for v, b, c in g[u]:
                edges.append((u, v, b, c))
                seen[v] = True
    def check(m):
        dp = [-1e8] * n
        dp[0] = 0.0
        for u, v, b, c in edges:
            dp[v] = max(dp[v], dp[u] + b - c * m)
        return dp[-1] >= 0.0
    
    l, r = 0.0, 1e4

    eps = 10 ** -10
    # 794 ms
    while r - l > eps:
        m = (l + r) * 0.5
        if check(m):
            l = m
        else:
            r = m

    '''
    for _ in range(50):
        m = (l + r) * 0.5
        if check(m):
            l = m
        else:
            r = m
    '''

    print(l)

solve()
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
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(m):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1
    
    q = []
    ans = 0
    for i, v in enumerate(deg):
        if v == 1:
            q.append((i, -1))
        elif v == 0:
            ans += 1
    while q:
        tmp = q
        q = []
        for u, p in tmp:
            if deg[u] == 0:
                ans += 1
                continue
            for v in g[u]:
                if v == p:
                    continue
                deg[v] -= 1
                if deg[v] == 1:
                    q.append((v, u))
    print(ans)


solve()

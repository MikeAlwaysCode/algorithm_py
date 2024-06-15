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
        g.append(input())

    fa = list(range(n * m))
    sz = [0] * (n * m)
    mn_r, mx_r, mn_c, mx_c = [n] * (n * m), [-1] * (n * m), [m] * (n * m), [-1] * (n * m)
    def find(x: int):
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            fa[cur], cur = x, fa[cur]
        return x
    
    def union(x: int, y: int):
        fx, fy = find(x), find(y)
        if fx == fy:
            return
        sz[fy] += sz[fx]
        fa[fx] = fy

    rcnt = [0] * n
    ccnt = [0] * m
    
    for i, row in enumerate(g):
        for j, c in enumerate(row):
            if c == '.':
                continue
            u = i * m + j
            sz[u] = 1
            if i and g[i - 1][j] == '#':
                v = (i - 1) * m + j
                union(u, v)
            if j and g[i][j - 1] == '#':
                v = i * m + j - 1
                union(u, v)

    for i, row in enumerate(g):
        for j, c in enumerate(row):
            if c == '.':
                rcnt[i] += 1
                ccnt[j] += 1
            else:
                u = find(i * m + j)
                mn_r[u] = min(mn_r[u], max(0, i - 1))
                mx_r[u] = max(mx_r[u], min(n - 1, i + 1))
                mn_c[u] = min(mn_c[u], max(0, j - 1))
                mx_c[u] = max(mx_c[u], min(m - 1, j + 1))

    cnt = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if g[i][j] == '.':
                continue
            u = i * m + j
            if find(u) != u:
                continue
            cnt[mn_r[u]][0] += sz[u]
            cnt[mx_r[u] + 1][0] -= sz[u]
            cnt[0][mn_c[u]] += sz[u]
            cnt[0][mx_c[u] + 1] -= sz[u]
            cnt[mn_r[u]][mn_c[u]] -= sz[u]
            cnt[mn_r[u]][mx_c[u] + 1] += sz[u]
            cnt[mx_r[u] + 1][mn_c[u]] += sz[u]
            cnt[mx_r[u] + 1][mx_c[u] + 1] -= sz[u]

    for i in range(n):
        for j in range(1, m):
            cnt[i][j] += cnt[i][j - 1]
            
    for i in range(1, n):
        for j in range(m):
            cnt[i][j] += cnt[i - 1][j]

    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(ans, cnt[i][j] + rcnt[i] + ccnt[j] - int(g[i][j] == '.'))
    print(ans)

for _ in range(int(input())):
    solve()

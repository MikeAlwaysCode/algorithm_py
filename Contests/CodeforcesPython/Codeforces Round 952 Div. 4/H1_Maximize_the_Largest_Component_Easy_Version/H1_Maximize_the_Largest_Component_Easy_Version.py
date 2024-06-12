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
            rcnt[i] += 1
            ccnt[j] += 1
            u = i * m + j
            sz[u] = 1
            if i and g[i - 1][j] == '#':
                v = (i - 1) * m + j
                union(u, v)
            if j and g[i][j - 1] == '#':
                v = i * m + j - 1
                union(u, v)
    
    ans = 0
    for i in range(n):
        res = m - rcnt[i]
        s = set()
        for j in range(m):
            if g[i][j] == '#':
                u = find(i * m + j)
                if u not in s:
                    s.add(u)
                    res += sz[u]
            else:
                if i and g[i - 1][j] == '#':
                    u = find((i - 1) * m + j)
                    if u not in s:
                        s.add(u)
                        res += sz[u]
                if i < n - 1 and g[i + 1][j] == '#':
                    u = find((i + 1) * m + j)
                    if u not in s:
                        s.add(u)
                        res += sz[u]
        ans = max(ans, res)
    for j in range(m):
        res = n - ccnt[j]
        s = set()
        for i in range(n):
            if g[i][j] == '#':
                u = find(i * m + j)
                if u not in s:
                    s.add(u)
                    res += sz[u]
            else:
                if j and g[i][j - 1] == '#':
                    u = find(i * m + j - 1)
                    if u not in s:
                        s.add(u)
                        res += sz[u]
                if j < m - 1 and g[i][j + 1] == '#':
                    u = find(i * m + j + 1)
                    if u not in s:
                        s.add(u)
                        res += sz[u]
        ans = max(ans, res)
    print(ans)


for _ in range(int(input())):
    solve()

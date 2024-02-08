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
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, m = mint()
    edges = []
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = mint()
        u -= 1
        v -= 1
        edges.append((u, v, w))
        g[u].append(v)
        g[v].append(u)
        
    fa = list(range(n + 1))
    def find(x: int):
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            fa[cur], cur = x, fa[cur]
        return x
 
    d = math.inf
    x = y = -1
    edges.sort(key = lambda x: -x[2])
    for u, v, w in edges:
        fu, fv = find(u), find(v)
        if fu == fv:
            d, x, y = w, u, v
        else:
            fa[fu] = fv
    
    ans = []
    fx = find(x)
    parent = [-1] * n
    q = [y]
    seen = [False] * n
    seen[y] = True
    while q:
        u = q.pop()
        for v in g[u]:
            if (u == y and v == x) or find(v) != fx or seen[v]:
                continue
            parent[v] = u
            seen[v] = True
            if v == x:
                q.clear()
                break
            q.append(v)
    while x != -1:
        ans.append(x + 1)
        x = parent[x]

    print(d, len(ans))
    print(*ans)

for _ in range(int(input())):
    solve()
import sys
from collections import deque

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
    g = [[] for _ in range(n)]
    deg = [0] * n
    root = -1
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1
        if root == -1 and len(g[u]) > 1:
            root = u
        if root == -1 and len(g[v]) > 1:
            root = v

    if n == 2:
        print(3)
        return

    parent = [-1] * n
    size = [1] * n
    s = [0] * n

    q = deque([root])
    while q:
        u = q.popleft()
        for v in g[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            q.append(v)
    q = deque([i for i in range(n) if deg[i] == 1])
    while q:
        u = q.popleft()
        s[u] += size[u]
        p = parent[u]
        if p == -1:
            continue
        s[p] += s[u]
        size[p] += size[u]
        deg[p] -= 1
        if p != root and deg[p] == 1:
            q.append(p)
    s[root] += size[root]
    # print(s)
    ans = 0

    # Reroot
    q = deque([(root, s[root])])
    while q:
        u, res = q.popleft()
        # print(u, res)
        ans = max(ans, res)
        for v in g[u]:
            if v == parent[u]:
                continue
            q.append((v, res - size[v] * 2 + n))
    
    print(ans)


solve()

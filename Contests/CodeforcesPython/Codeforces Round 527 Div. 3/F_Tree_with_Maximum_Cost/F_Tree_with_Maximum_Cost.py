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
    a = ints()
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1

    parent = [-1] * n
    vals = a[:]
    s = [0] * n

    q = deque([0])
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
        p = parent[u]
        if p == -1:
            continue
        vals[p] += vals[u]
        s[p] += s[u] + vals[u]
        deg[p] -= 1
        if p != 0 and deg[p] == 1:
            q.append(p)
    # print(vals)
    ans = 0

    # Reroot
    q = deque([(0, s[0])])
    while q:
        u, res = q.popleft()
        # print(u, res)
        ans = max(ans, res)
        for v in g[u]:
            if v == parent[u]:
                continue
            q.append((v, res - vals[v] * 2 + vals[0]))
    
    print(ans)


solve()

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
    for _ in range(n - 1):
        u, v = mint()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
        deg[u - 1] += 1
        deg[v - 1] += 1
    
    def bfs(start: int, dist: list) -> int:
        dist[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in g[u]:
                if dist[v] != -1:
                    continue
                dist[v] = dist[u] + 1
                q.append(v)
        return u
    
    dist0 = [-1] * n
    dist1 = [-1] * n
    dist2 = [-1] * n
    L = bfs(0, dist0)
    R = bfs(L, dist1)
    bfs(R, dist2)
    q = deque(list(u for u, d in enumerate(deg) if d == 1 and u != L and u != R))
    ans = 0
    op = []
    while q:
        u = q.popleft()
        if dist1[u] >= dist2[u]:
            ans += dist1[u]
            op.append((u, L))
        else:
            ans += dist2[u]
            op.append((u, R))
        for v in g[u]:
            deg[v] -= 1
            if deg[v] == 1:
                q.append(v)
    q = deque([R])
    while q:
        u = q.popleft()
        ans += dist1[u]
        op.append((u, L))
        for v in g[u]:
            deg[v] -= 1
            if deg[v] == 1:
                q.append(v)
    print(ans)
    for u, v in op:
        print(u + 1, v + 1, u + 1)


solve()

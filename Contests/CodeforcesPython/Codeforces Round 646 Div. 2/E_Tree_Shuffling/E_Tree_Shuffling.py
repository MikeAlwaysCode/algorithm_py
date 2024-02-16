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
    a = [0] * n
    cnt = [[0] * 2 for _ in range(n)]
    for i in range(n):
        a[i], b, c = mint()
        if b != c:
            cnt[i][c] += 1
    g = [[] for _ in range(n)]
    # deg = [0] * n
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        # deg[u] += 1
        # deg[v] += 1
    parent = [-1] * n
    q = deque([(0, -1)])
    s = [0]
    while q:
        u, p = q.popleft()
        for v in g[u]:
            if v == p:
                continue
            s.append(v)
            parent[v] = u
            a[v] = min(a[v], a[u])
            q.append((v, u))
    ans = 0
    # q = deque([i for i in range(1, n) if deg[i] == 1])
    # while q:
    #     u = q.popleft()
    #     m = min(cnt[u])
    #     ans += a[u] * m * 2
    #     if u == 0:
    #         break
    #     p = parent[u]
    #     cnt[p][0] += cnt[u][0] - m
    #     cnt[p][1] += cnt[u][1] - m
    #     deg[p] -= 1
    #     if (p != 0 and deg[p] == 1) or deg[p] == 0:
    #         q.append(p)
    for u in s[::-1]:
        m = min(cnt[u])
        ans += a[u] * m * 2
        if parent[u] != -1:
            cnt[parent[u]][0] += cnt[u][0] - m
            cnt[parent[u]][1] += cnt[u][1] - m
    print(-1 if cnt[0][0] != cnt[0][1] else ans)


solve()

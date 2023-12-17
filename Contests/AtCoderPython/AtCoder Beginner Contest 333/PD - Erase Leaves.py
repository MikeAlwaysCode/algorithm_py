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
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        deg[u] += 1
        deg[v] += 1
        g[u].append(v)
        g[v].append(u)

    if deg[0] == 1:
        print(1)
        return

    cnt = [1] * n
    q = deque([i for i in range(n) if deg[i] == 1])
    while q:
        u = q.popleft()
        for v in g[u]:
            if deg[v] == 1 and v != 0:
                continue
            cnt[v] += cnt[u]
            deg[v] -= 1
            if deg[v] == 1 and v != 0:
                q.append(v)
    print(cnt[0] - max(cnt[i] for i in g[0]))


solve()

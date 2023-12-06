import sys
from collections import *

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
    g = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    bad = [False] * (n + 1)
    for _ in range(n - 1):
        u, v, w = mint()
        deg[u] += 1
        deg[v] += 1
        if w == 1:
            g[u].append(v)
            g[v].append(u)
        else:
            bad[u] = bad[v] = True

    q = deque([i for i in range(2, n + 1) if deg[i] == 1])
    ans = []
    while q:
        u = q.popleft()
        if bad[u]:
            ans.append(u)
        for v in g[u]:
            if v == 1 or deg[v] == 1:
                continue
            deg[v] -= 1
            if deg[v] == 1:
                q.append(v)

    print(len(ans))
    print(*ans)


solve()

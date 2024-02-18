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
    n, m = mint()
    g = [[] for _ in range(n)]
    deg = [0] * n
    dp = [0] * n
    for _ in range(m):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        deg[v] += 1
    
    q = deque(list(i for i, v in enumerate(deg) if v == 0))
    while q:
        u = q.popleft()
        for v in g[u]:
            dp[v] = max(dp[v], dp[u] + 1)
            deg[v] -= 1
            if deg[v] == 0:
                q.append(v)
    
    print(max(dp))


solve()

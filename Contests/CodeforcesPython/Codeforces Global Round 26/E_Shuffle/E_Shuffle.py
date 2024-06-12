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
    deg = [0] * n
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1
    parent = [-1] * n
    q = deque([0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            q.append(v)
    dp = [[0] * 2 for _ in range(n)]
    for u in order[::-1]:
        dp[u][1] += int(deg[u] == 1)
        if (p := parent[u]) != -1:
            dp[p][0] += max(dp[u])




for _ in range(int(input())):
    solve()

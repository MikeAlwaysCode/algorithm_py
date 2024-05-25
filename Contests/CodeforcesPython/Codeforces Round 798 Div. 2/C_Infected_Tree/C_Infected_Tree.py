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
    for _ in range(n - 1):
        u, v = mint()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    
    order = []
    parent = [-1] * n
    q = deque([0])
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            q.append(v)
    dp = [[0] * 2 for _ in range(n)]
    sz = [1] * n
    for u in order[::-1]:
        if (p := parent[u]) != -1:
            sz[p] += sz[u]
            if dp[p][0] == 0:
                dp[p][0], dp[p][1] = sz[u] - 1, dp[u][0]
            else:
                dp[p][0] = max(dp[p][0] + dp[u][0], dp[p][1] + sz[u] - 1)
    print(dp[0][0])


for _ in range(int(input())):
    solve()

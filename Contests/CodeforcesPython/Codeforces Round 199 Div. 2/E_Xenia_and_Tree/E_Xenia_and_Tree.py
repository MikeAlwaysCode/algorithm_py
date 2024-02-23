import math
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

# def solve() -> None:
n, m = mint()

g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = mint()
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

k = n.bit_length()
parent = [[0] * n for _ in range(k)]
depth = [-1] * n
depth[0] = 0

q = [0]
while q:
    u = q.pop()
    for v in g[u]:
        if depth[v] >= 0:continue
        depth[v] = depth[u] + 1
        parent[0][v] = u
        q.append(v)
        
for i in range(1, k):
    for j in range(n):
        if (p := parent[i - 1][j]) != -1:
            parent[i][j] = parent[i-1][p]

def go_up(u, k):
    for i in range(k.bit_length()):
        if (k >> i) & 1:
            u = parent[i][u]
    return u

def lca(u, v):
    d = depth[u] - depth[v]
    if d >= 0:
        u = go_up(u, d)
    else:
        v = go_up(v, -d)
    if u == v: return u
    for p in range(k-1, -1, -1):
        if parent[p][u] != parent[p][v]:
            u, v = parent[p][u], parent[p][v]
    return parent[0][u]

def dist(u, v):
    return depth[u] + depth[v] - depth[lca(u, v)] * 2

red_nodes = [0]
dis = [math.inf] * n

for _ in range(m):
    t, u = mint()
    u -= 1
    if t == 1:
        red_nodes.append(u)
    else:
        if len(red_nodes) >= 100:
            q = deque(red_nodes)
            for x in red_nodes:
                dis[x] = 0
            while q:
                x = q.popleft()
                for y in g[x]:
                    if dis[x] + 1 < dis[y]:
                        dis[y] = dis[x] + 1
                        q.append(y)
            red_nodes = []
    
        ans = dis[u]
        for v in red_nodes:
            # ans = min(ans, lca.dist(u, v))
            ans = min(ans, dist(u, v))
        print(ans)

# solve()

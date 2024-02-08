import math
import sys
from heapq import *

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
    n, m, k = mint()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, d = mint()
        u -= 1
        v -= 1
        g[u].append((v, d))
        g[v].append((u, d))
    
    ans = 0
    dis = [math.inf] * n
    dis[0] = 0
    q = [(0, 0, 0)]
    for _ in range(k):
        u, d = mint()
        q.append((d, 1, u - 1))
    
    heapify(q)
    while q:
        d, t, u = heappop(q)
        if d > dis[u] or (d == dis[u] and t == 1):
            ans += t
            continue
        dis[u] = d
        for v, w in g[u]:
            if d + w >= dis[v]:
                continue
            dis[v] = d + w
            heappush(q, (d + w, 0, v))
    
    print(ans)


solve()

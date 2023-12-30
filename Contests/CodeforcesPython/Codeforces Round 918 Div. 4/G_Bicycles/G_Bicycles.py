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
    n, m = mint()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = mint()
        u -= 1
        v -= 1
        g[u].append((v, w))
        g[v].append((u, w))
    
    s = ints()

    dis = [math.inf] * n
    dis[0] = 0
    def dijkstra(g: list, start: int, s: int):
        dist = [math.inf] * n
        dist[start] = dis[start]
        h = [(dist[start], start)]
        while h:
            d, x = heappop(h)
            if d > dist[x]:
                continue
            for y, wt in g[x]:
                new_d = dist[x] + wt * s
                if new_d < dist[y]:
                    dist[y] = new_d
                    heappush(h, (new_d, y))
        for i in range(n):
            if dis[i] > dist[i]:
                dis[i] = dist[i]
    
    idx = sorted(range(n), key = lambda x: -s[x])
    dijkstra(g, 0, s[0])
    for x in idx:
        if x == 0 or x == n - 1:
            continue
        dijkstra(g, x, s[x])
    print(dis[-1])


for _ in range(int(input())):
    solve()

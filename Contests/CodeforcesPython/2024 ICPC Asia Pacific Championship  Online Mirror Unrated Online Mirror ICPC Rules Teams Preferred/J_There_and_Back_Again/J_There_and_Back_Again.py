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
        g[u - 1].append((v - 1, w))
        g[v - 1].append((u - 1, w))
    
    dist = [math.inf] * n
    more = math.inf
    dist[0] = 0
    h = [(0, 0)]
    p = [-1] * n
    while h:
        d, u = heappop(h)
        if d > dist[u]:
            # more = min(more, d - dist[u])
            continue
        for v, w in g[u]:
            if v == p[u]:
                continue
            nd = d + w
            # if nd >= dist[v]:
            #     more = min(more, nd - dist[v])
            # else:
                # if dist[v] != math.inf:
                #     more = min(more, dist[v] - nd)
            if nd < dist[v]:
                p[v] = u
                dist[v] = nd
                heappush(h, (nd, v))
    
    # if more != math.inf:
    #     print(dist[-1] * 2 + more)
    #     return
    
    s = set()
    u = n - 1
    while u >= 0:
        s.add(u)
        u = p[u]

    for u in s:
        for v, w in g[u]:
            # if v not in s:
            #     more = min(more, w * 2)
            if p[u] != v and (p[v] != u or v not in s):
                more = min(more, dist[v] + w - dist[u], w * 2)

    print(-1 if more == math.inf else dist[-1] * 2 + more)


solve()

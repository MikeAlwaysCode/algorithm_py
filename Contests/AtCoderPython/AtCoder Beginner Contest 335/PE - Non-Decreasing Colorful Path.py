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
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n, m = mint()
    val = ints()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    dis = [0] * n
    dis[0] = 1
    q = [(val[0], 0, 1)]
    while q:
        v, x, d = heappop(q)
        if d < dis[x]:
            continue
        for y in g[x]:
            if val[y] < val[x]:
                continue
            nd = d + 1 if val[y] > val[x] else d
            if nd <= dis[y]:
                continue
            dis[y] = nd
            if y < n - 1:
                heappush(q, (val[y], y, nd))
    print(dis[-1])


solve()

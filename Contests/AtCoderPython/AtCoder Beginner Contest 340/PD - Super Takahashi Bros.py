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
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    dis = [math.inf] * n
    dis[0] = 0
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b, x = mint()
        g[i].append((i + 1, a))
        g[i].append((x - 1, b))
    
    h = [(0, 0)]
    while h:
        d, u = heappop(h)
        if d > dis[u]:
            continue
        for v, w in g[u]:
            if d + w < dis[v]:
                dis[v] = d + w
                heappush(h, (dis[v], v))
    print(dis[-1])


solve()

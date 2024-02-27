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
    g = [[] for _ in range(n)]
    for _ in range(m):
        l, d, k, c, a, b = mint()
        a -= 1
        b -= 1
        g[b].append((l, d, k, c, a))

    dis = [-1] * n
    q = []

    for l, d, k, c, a in g[-1]:
        t = l + d * (k - 1)
        if t < dis[a]:
            continue
        dis[a] = t
        heappush(q, (-t, a))

    while q:
        t, b = heappop(q)
        t = -t
        if t < dis[b]:
            continue
        for l, d, k, c, a in g[b]:
            m = min(k - 1, (t - c - l) // d)
            nt = l + d * m
            if nt > dis[a]:
                dis[a] = nt
                heappush(q, (-nt, a))
    
    for i in range(n - 1):
        if dis[i] == -1:
            print("Unreachable")
        else:
            print(dis[i])


solve()

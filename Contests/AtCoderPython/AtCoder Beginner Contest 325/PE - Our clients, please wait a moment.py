import sys
import math
from heapq import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, a, b, c = mint()
    g = []
    for _ in range(n):
        g.append(ints())
    dis = [math.inf] * n 
    dis[0] = 0
    q = [(0, 0)]
    while q:
        d, x = heappop(q)
        if d > dis[x]:
            continue
        for y in range(n):
            if x == y: continue
            new_d = dis[x] + g[x][y] * a
            if new_d < dis[y]:
                dis[y] = new_d
                heappush(q, (new_d, y))
    # print(dis)
    q = [(dis[x], x) for x in range(n)]
    heapify(q)
    while q:
        d, x = heappop(q)
        if d > dis[x]:
            continue
        for y in range(n):
            if x == y: continue
            new_d = dis[x] + g[x][y] * b + c
            if new_d < dis[y]:
                dis[y] = new_d
                heappush(q, (new_d, y))

    print(dis[-1])

solve()
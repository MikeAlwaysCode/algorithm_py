import math
import sys
from bisect import *
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
    n, t = mint()
    g = [[] for _ in range(n)]
    for i in range(t):
        m = sint()
        for _ in range(m):
            u, v = mint()
            u -= 1
            v -= 1
            g[u].append((v, i))
            g[v].append((u, i))

    k = sint()
    times = ints()
    
    dis = [math.inf] * n
    dis[0] = 0

    t_pos = [[] for _ in range(t)]
    for i, x in enumerate(times, 1):
        t_pos[x - 1].append(i)
    
    h = [(0, 0)]
    while h:
        d, x = heappop(h)
        if d > dis[x]: continue
        for y, i in g[x]:
            j = bisect(t_pos[i], d)
            if j >= len(t_pos[i]) or t_pos[i][j] >= dis[y]:
                continue
            dis[y] = t_pos[i][j]
            heappush(h, (dis[y], y))

    '''
    point = [set() for _ in range(t)]
    for y, i in g[0]:
        point[i].add(y)
    
    for i, t in enumerate(times, 1):
        t -= 1
        if not point[t]: continue
        p = point[t].copy()
        point[t].clear()
        for x in p:
            if dis[x] < i: continue
            dis[x] = i
            for y, j in g[x]:
                point[j].add(y)
    '''
    
    print(-1 if dis[-1] == math.inf else dis[-1])

solve()
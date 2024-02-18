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

def ext_gcd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, g = ext_gcd(b, a % b)
    x, y = y, x - a // b * y
    return x, y, g

def solve() -> None:
    n, m, h = mint()
    l = ints()
    s = ints()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    dis = [math.inf] * n
    dis[0] = 0
    q = [(0, 0)]
    while q:
        t, u = heappop(q)
        if t > dis[u]:
            continue
        for v in g[u]:
            c = ((l[v] + s[v] * t) % h - (l[u] + s[u] * t) % h) % h
            
            if c == 0:
                nt = t
            else:
                # c = (l[v] - l[u]) % h
                d = s[u] - s[v]
                x, y, gg = ext_gcd(d, h)
                if c % gg:
                    continue
                e = h // gg
                x = x * c // gg % e
                nt = t + x
            if nt + 1 < dis[v]:
                dis[v] = nt + 1
                heappush(q, (nt + 1, v))
    
    print(-1 if dis[-1] == math.inf else dis[-1])


for _ in range(int(input())):
    solve()

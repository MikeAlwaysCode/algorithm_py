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

def solve() -> None:
    n = sint()
    c = []
    for _ in range(3):
        c.append(ints())
    check = True
    deg = [0] * n
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1
        if check and (deg[u] > 2 or deg[v] > 2):
            check = False
    
    if not check:
        print(-1)
        return
    
    fst = 0
    while deg[fst] > 1:
        fst += 1
    sec = g[fst][0]
    
    q = deque()
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            q.append((sec, fst, j + 1, i + 1, c[i][fst] + c[j][sec]))
    
    ans = math.inf
    fc = sc = -1
    while q:
        u, p, uc, pc, cost = q.popleft()
        if len(g[u]) == 1:
            if cost < ans:
                ans, fst, sec, fc, sc = cost, u, p, uc, pc
            continue
        tc = uc ^ pc
        for v in g[u]:
            if v == p:
                continue
            q.append((v, u, tc, uc, cost + c[tc - 1][v]))

    col = [0] * n
    col[fst], col[sec] = fc, sc
    q = deque([(sec, fst)])
    while q:
        u, p = q.popleft()
        for v in g[u]:
            if v == p:
                continue
            col[v] = col[u] ^ col[p]
            q.append((v, u))

    print(ans)
    print(*col)


solve()
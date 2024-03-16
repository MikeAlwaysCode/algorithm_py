import math
import sys
from collections import Counter
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
        u, v, c = mint()
        g[u - 1].append((v - 1, c))
        g[v - 1].append((u - 1, c))
    x, y = mint()
    if x == y:
        print(0)
        return
    x -= 1
    y -= 1
    seen = [False] * n
    seen[x] = True
    q = [x]
    ans = 0
    s = set()
    while q:
        tmp = q
        q, to = [], []
        ans += 1
        for u in tmp:
            for v, c in g[u]:
                s.add(c)
 
        while tmp:
            u = tmp.pop()
            if u == y:
                print(ans)
                return
            for v, c in g[u]:
                if seen[v]:
                    continue
                if c in s:
                    seen[v] = True
                    tmp.append(v)
                else:
                    to.append(v)
        
        for u in to:
            if seen[u]:
                continue
            seen[u] = True
            q.append(u)

    '''
    seen = [math.inf] * n
    seen[x] = 0
    col = Counter()
    q = [(0, x)]
    while q:
        t, u = heappop(q)
        if t > seen[u]:
            continue
        for v, c in g[u]:
            if col[c] == 0:
                col[c] = seen[u] + 1
            else:
                col[c] = min(col[c], seen[u] + 1)
            if seen[v] <= col[c]:
                continue
            seen[v] = col[c]
            heappush(q, (seen[v], v))

    print(seen[y])
    '''


for _ in range(int(input())):
    solve()

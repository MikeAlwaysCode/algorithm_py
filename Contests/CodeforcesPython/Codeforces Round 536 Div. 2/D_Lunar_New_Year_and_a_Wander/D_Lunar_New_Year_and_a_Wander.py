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
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = mint()
        g[u].append(v)
        g[v].append(u)
        
    ans = []
    h = [1]
    seen = [False] * (n + 1)
    seen[1] = True
    while h:
        u = heappop(h)
        ans.append(u)
        for v in g[u]:
            if seen[v]: continue
            seen[v] = True
            heappush(h, v)
    print(*ans)

solve()
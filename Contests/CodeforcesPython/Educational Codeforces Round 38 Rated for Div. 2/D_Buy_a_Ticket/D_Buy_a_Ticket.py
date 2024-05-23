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
    ans = ints()
    h = list((v, i) for i, v in enumerate(ans))
    heapify(h)
    while h:
        d, x = heappop(h)
        if d > ans[x]:
            continue
        for y, w in g[x]:
            if d + 2 * w < ans[y]:
                ans[y] = d + 2 * w
                heappush(h, (ans[y], y))
    print(*ans)


solve()

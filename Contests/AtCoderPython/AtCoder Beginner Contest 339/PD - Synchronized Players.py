import math
import sys
# from heapq import *

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    g = []
    init = []
    for i in range(n):
        g.append(input())
        for j, c in enumerate(g[-1]):
            if c == 'P':
                init.append(i * n + j)
    dis = [[math.inf] * (n * n) for _ in range(n * n)]
    p1, p2 = init[0], init[1]
    dis[p1][p2] = d = 0
    q = [(p1, p2)]
    ans = math.inf
    while q:
        tmp = q
        q = []
        for p1, p2 in tmp:
            if d > dis[p1][p2]:
                continue
            x1, y1 = divmod(p1, n)
            x2, y2 = divmod(p2, n)
            for dx, dy in DIR:
                nx1, ny1, nx2, ny2 = x1, y1, x2, y2
                if 0 <= nx1 + dx < n and 0 <= ny1 + dy < n and g[nx1 + dx][ny1 + dy] != '#':
                    nx1 += dx
                    ny1 += dy
                if 0 <= nx2 + dx < n and 0 <= ny2 + dy < n and g[nx2 + dx][ny2 + dy] != '#':
                    nx2 += dx
                    ny2 += dy
                p1, p2 = nx1 * n + ny1, nx2 * n + ny2
                if p1 == p2:
                    ans = d + 1
                    break
                elif d + 1 < dis[p1][p2]:
                    dis[p1][p2] = d + 1
                    q.append((p1, p2))
        if ans != math.inf:
            break
        d += 1
    print(-1 if ans == math.inf else ans)


solve()

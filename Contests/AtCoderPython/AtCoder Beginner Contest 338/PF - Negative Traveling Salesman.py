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
    n, m = mint()
    # neg = [False] * n
    g = [[math.inf] * n for _ in range(n)]
    for _ in range(m):
        u, v, w = mint()
        u -= 1
        v -= 1
        g[u][v] = w
        # if w < 0:
        #     neg[u] = True

    # q = []
    # dp = [[math.inf] * n for _ in range(1 << n)]
    # for i in range(n):
    #     dp[1 << i][i] = 0
    #     heappush(q, (0, 1 << i, i, [i]))
    # mx = (1 << n) - 1
    # ans = math.inf
    # ans_path = []
    # while q:
    #     d, s, u, path = heappop(q)
    #     if d > dp[s][u]:
    #         continue
    #     for v in range(n):
    #         if u == v or g[u][v] == math.inf:
    #             continue
    #         if d + g[u][v] < dp[s | (1 << v)][v]:
    #             mask = s | (1 << v)
    #             dp[mask][v] = d + g[u][v]
    #             if mask == mx:
    #                 if dp[mask][v] < ans:
    #                     ans_path = path[:] + [v]
    #                 ans = min(ans, dp[mask][v])
    #             if mask != mx or neg[v]:
    #                 heappush(q, (dp[mask][v], mask, v, path[:] + [v]))
    # print("No" if ans == math.inf else ans)
    # print(ans_path)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    dp = [[math.inf] * n for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i][i] = 0
    for s in range(2, 1 << n):
        for i in range(n):
            if not (s >> i) & 1:
                continue
            for j in range(n):
                if not (s >> j) & 1 or g[j][i] == math.inf:
                    continue
                dp[s][i] = min(dp[s][i], min(dp[s][j], dp[s ^ (1 << i)][j]) + g[j][i])
                
    ans = min(dp[-1])
    # print(dp[-1])
    print("No" if ans == math.inf else ans)

solve()

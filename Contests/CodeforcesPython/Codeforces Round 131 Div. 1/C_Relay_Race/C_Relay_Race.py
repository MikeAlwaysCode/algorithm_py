import math
import sys

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
    g = []
    for _ in range(n):
        g.append(ints())
    
    dp = [[-math.inf] * n for _ in range(n)]
    dp[0][0] = g[0][0]
    for k in range(1, n * 2 - 1):
        for x1 in range(min(n - 1, k), max(-1, k - n), -1):
            y1 = k - x1
            for x2 in range(min(n - 1, k), x1 - 1, -1):
                y2 = k - x2
                if x1:
                    dp[x1][x2] = max(dp[x1][x2], dp[x1 - 1][x2])
                if x2:
                    dp[x1][x2] = max(dp[x1][x2], dp[x1][x2 - 1])
                if x1 and x2:
                    dp[x1][x2] = max(dp[x1][x2], dp[x1 - 1][x2 - 1])
                dp[x1][x2] += g[x1][y1]
                if x1 != x2:
                    dp[x1][x2] += g[x2][y2]
    print(dp[-1][-1])
                

solve()

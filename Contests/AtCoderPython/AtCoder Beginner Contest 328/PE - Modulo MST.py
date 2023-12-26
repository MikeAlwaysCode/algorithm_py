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
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, m, k = mint()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = mint()
        u -= 1
        v -= 1
        g[u].append((v, w))
        g[v].append((u, w))
    
    dp = [set() for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i].add(0)
    for mask in range(1, 1 << n):
        for i in range(n):
            if not (mask >> i) & 1:
                continue
            for x in dp[mask]:
                for j, w in g[i]:
                    if (mask >> j) & 1 == 0:
                        dp[mask | (1 << j)].add((x + w) % k)
    print(min(dp[-1]))
    


solve()
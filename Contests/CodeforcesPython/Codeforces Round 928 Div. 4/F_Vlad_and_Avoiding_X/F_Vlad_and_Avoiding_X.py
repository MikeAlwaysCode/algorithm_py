import math
import sys
# from collections import defaultdict

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
DIR = ((-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1))

def solve() -> None:
    g = [sum((c == 'B') << i for i, c in enumerate(input())) for _ in range(7)]
    buc = [[] for _ in range(2)]
    d = dict()
    for i in range(1, 6):
        cur = g[i] & (g[i - 1] >> 1) & (g[i - 1] << 1) & (g[i + 1] >> 1) & (g[i + 1] << 1)
        for j in range(1, 6):
            if (cur >> j) & 1:
                m = (i + j) & 1
                d[(i, j)] = len(buc[m])
                buc[m].append((i, j))

    mat = [set() for _ in range(2)]
    for i in range(1, 6):
        for j in range(1, 6):
            m = (i + j) & 1
            mask = 0
            for dx, dy in DIR:
                ni, nj = i + dx, j + dy
                if (ni, nj) in d:
                    mask |= 1 << d[(ni, nj)]
            if mask != mask & -mask:
                mat[m].add(mask)
    
    ans = 0
    for m in range(2):
        if not buc[m]:
            continue
        n = len(buc[m])
        dp = [math.inf] * (1 << n)
        mx = (1 << n) - 1
        dp[0] = 0
        for mask in range(1, 1 << n):
            for j in range(n):
                if not (mask >> j) & 1:
                    continue
                dp[mask] = min(dp[mask], dp[mask ^ (1 << j)] + 1)
                for umask in mat[m]:
                    if not (umask >> j) & 1:
                        continue
                    umask ^= mx
                    dp[mask] = min(dp[mask], dp[mask & umask] + 1)
                
        ans += dp[-1]

    print(ans)

for _ in range(int(input())):
    solve()

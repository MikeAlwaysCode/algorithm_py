import math
import sys
from functools import cache

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

lcms = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 18, 20, 21, 24, 28, 30, 35, 36, 40, 42, 45, 56, 60, 63, 70, 72, 84, 90, 105, 120, 126, 140, 168, 180, 210, 252, 280, 315, 360, 420, 504, 630, 840, 1260, 2520]
idx = {v:i for i, v in enumerate(lcms)}
lcm_trans = [[0] * 10 for _ in range(len(lcms))]
for i, v in enumerate(lcms):
    lcm_trans[i][0] = lcm_trans[i][1] = i
    for j in range(2, 10):
        lcm_trans[i][j] = idx[math.lcm(v, j)]

dp = [[[-1] * 2520 for _ in range(len(lcms))] for _ in range(20)]

def solve() -> None:
    L, R = mint()
    l, r = [], []
    while L:
        l.append(L % 10)
        L //= 10
    while R:
        r.append(R % 10)
        R //= 10

    n = len(r)
    if len(l) < len(r):
        l.extend([0] * (len(r) - len(l)))

    def dfs(i: int, j: int, rem: int, limit_low: bool, limit_high: bool) -> int:
        if i < 0:
            return rem % lcms[j] == 0
        
        if not limit_low and not limit_high and dp[i][j][rem] != -1:
            return dp[i][j][rem]

        # 第 i 个数位可以从 lo 枚举到 hi
        # 如果对数位还有其它约束，应当只在下面的 for 循环做限制，不应修改 lo 或 hi
        lo = l[i] if limit_low else 0
        hi = r[i] if limit_high else 9
        res = 0
        for d in range(lo, hi + 1):
            res += dfs(i - 1, lcm_trans[j][d], (rem * 10 + d) % 2520, limit_low and d == lo, limit_high and d == hi)
        if not limit_low and not limit_high:
            dp[i][j][rem] = res
        return res

    print(dfs(n - 1, 0, 0, True, True))

for _ in range(sint()):
    solve()

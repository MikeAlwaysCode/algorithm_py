import sys
import math

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    nums = ints()
    l1, c1, k1 = mint()
    l2, c2, k2 = mint()

    dp = [[math.inf] * (k1 + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i, d in enumerate(nums):
        for j in range(k1 + 1):
            for nj in range(j, k1 + 1):
                dp[i + 1][nj] = min(dp[i + 1][nj], dp[i][j] + max((d - (nj - j) * l1 + l2 - 1), 0) // l2)

    ans = math.inf
    for i in range(k1 + 1):
        if dp[n][i] > k2: continue
        ans = min(ans, i * c1 + dp[n][i] * c2)
    
    print(-1 if ans == math.inf else ans)

solve()
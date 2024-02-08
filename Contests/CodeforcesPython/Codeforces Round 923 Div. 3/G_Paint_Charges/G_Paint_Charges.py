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
    nums = ints()
    dp = [[[math.inf] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 0
    # 到第i个点，左边最远没有上色的距离j，右边最近没有上色的距离k
    for i in range(n):
        for j in range(n):
            for k in range(n + 1):
                if dp[i][j][k] == math.inf:
                    continue
                ni = i + 1
                # not paint
                nj = j + 1 if j > 0 else 1 if k == 0 else 0
                nk = max(0, k - 1)
                dp[ni][nj][nk] = min(dp[ni][nj][nk], dp[i][j][k])

                # paint to left
                nj = j + 1 if j > 0 else 0
                if nj <= nums[i]:
                    nj = 0
                nk = max(0, k - 1)
                dp[ni][nj][nk] = min(dp[ni][nj][nk], dp[i][j][k] + 1)

                # paint to right
                nj = j + 1 if j > 0 else 0
                nk = max(nums[i] - 1, k - 1)
                dp[ni][nj][nk] = min(dp[ni][nj][nk], dp[i][j][k] + 1)
    print(min(dp[n][0]))


for _ in range(int(input())):
    solve()

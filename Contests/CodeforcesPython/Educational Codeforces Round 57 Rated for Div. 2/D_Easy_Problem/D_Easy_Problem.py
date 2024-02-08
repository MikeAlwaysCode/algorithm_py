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


t = "hard"

def solve() -> None:
    n = sint()
    s = input()
    nums = ints()
    dp = [[math.inf] * 5 for _ in range(n + 1)]
    dp[0][0] = 0
    for i, c in enumerate(s):
        for j in range(4):
            if c != t[j]:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
            else:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + nums[i])
                dp[i + 1][j + 1] = dp[i][j]
    print(min(dp[-1][:4]))

solve()

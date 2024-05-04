import sys
from itertools import accumulate

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
    n, k = mint()
    nums = ints()
    pres = list(accumulate(nums, initial=0))
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i, x in enumerate(nums):
        for j in range(1, k + 1):
            if i - j < 0:
                break
            x = min(x, nums[i - j])
            dp[i + 1][j] = pres[i + 1] - pres[i - j] - x * (j + 1)
        
        for j in range(k, 0, -1):
            if i - j >= 0:
                for jj in range(k - j + 1):
                    dp[i + 1][j + jj] = max(dp[i + 1][j + jj], dp[i + 1][j] + dp[i - j][jj])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            
                
    print(pres[-1] - max(dp[-1]))


for _ in range(int(input())):
    solve()

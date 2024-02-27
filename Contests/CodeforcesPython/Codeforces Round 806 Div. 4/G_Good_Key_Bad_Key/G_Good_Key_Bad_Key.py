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
    n, k = mint()
    nums = ints()
    dp = [0] * 32
    for i, x in enumerate(nums):
        dp[31] = max(dp[31], dp[30])
        for j in range(min(30, i + 1), 0, -1):
            dp[j] = max(dp[j] + (x >> j) - k, dp[j - 1] + (x >> j))
        dp[0] += x - k
    print(max(dp))

for _ in range(int(input())):
    solve()

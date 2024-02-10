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
    n = sint()
    nums = ints()
    dp = [0] * n
    dp[0], dp[1] = 0, abs(nums[0] - nums[1])
    for i in range(2, n):
        dp[i] = min(dp[i - 1] + abs(nums[i - 1] - nums[i]), dp[i - 2] + abs(nums[i - 2] - nums[i]))
    print(dp[-1])


solve()

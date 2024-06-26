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
    dp = [0] * (n + 1)
    for i in range(1, n - 1, 2):
        dp[i + 1] = dp[i - 1] + max(max(nums[i - 1], nums[i + 1]) + 1 - nums[i], 0)
    ans = dp[n - 1] if n & 1 else dp[n - 2]
    if not n & 1:
        suff = 0
        for i in range(n - 2, 0, -2):
            suff += max(max(nums[i - 1], nums[i + 1]) + 1 - nums[i], 0)
            ans = min(ans, suff + dp[i - 2])
    print(ans)


for _ in range(int(input())):
    solve()

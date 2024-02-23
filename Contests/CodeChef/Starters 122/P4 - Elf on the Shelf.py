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
    n = sint()
    nums = ints()
    if n == 2:
        print((nums[1] - nums[0]) / 2, 1)
        return
    
    dp = [math.inf] * (n + 1)

    dp[0], dp[2], dp[3] = 0, nums[1] - nums[0], nums[2] - nums[0]
    for i in range(3, n):
        dp[i + 1] = min(max(nums[i] - nums[i - 1], dp[i - 1]), max(nums[i] - nums[i - 2], dp[i - 2]))
    
    res = dp[-1] / 2
    cnt, l = 1, 0
    for r in range(n):
        if nums[r] - nums[l] > dp[-1]:
            cnt += 1
            l = r

    print(res, cnt)


for _ in range(sint()):
    solve()

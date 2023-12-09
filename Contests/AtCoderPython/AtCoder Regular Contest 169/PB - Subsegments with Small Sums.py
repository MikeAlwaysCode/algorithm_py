import sys
from bisect import *

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
    n, s = mint()
    nums = ints()
    ans = cur = 0
    dp = list(range(n + 1))
    pres = [0]
    for i, x in enumerate(nums, 1):
        cur += x
        if cur >= s:
            j = bisect_left(pres, cur - s)
            dp[i] += dp[j]
        pres.append(cur)
        ans += dp[i]
    # print(pres)
    # print(dp)
    print(ans)
    #
    # dp2 = [0] * (n + 1)
    # for l in range(n):
    #     for r in range(l, n):
    #         res, cur = 1, 0
    #         for i in range(l, r + 1):
    #             cur += nums[i]
    #             if cur > s:
    #                 res += 1
    #                 cur = nums[i]
    #         dp2[r + 1] += res
    # print(sum(dp2))
    # print(dp)
    # print(dp2)


solve()

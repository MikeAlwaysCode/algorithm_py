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
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n, k = mint()
    nums = ints()
    if k > 2:
        print(0)
        return
    nums.sort()
    ans = min(nums[0], min(nums[i] - nums[i - 1] for i in range(1, n)))
    if k == 2:
        for i in range(n):
            for j in range(i, n):
                x = nums[i] + nums[j]
                k = bisect(nums, x)
                if k < n:
                    ans = min(ans, nums[k] - x)
                if k:
                    ans = min(ans, x - nums[k - 1])
    print(ans)


for _ in range(int(input())):
    solve()

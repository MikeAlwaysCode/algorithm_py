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
    n, k = mint()
    nums = ints()
    nums.sort()
    if nums[0] == nums[-1]:
        print(0)
        return
    if nums[0] <= k <= nums[-1]:
        print(-1)
        return
    ans = g = 0
    for x in nums:
        ans += abs(x - k)
        g = math.gcd(g, abs(x - k))
    print(ans // g - n)


for _ in range(int(input())):
    solve()

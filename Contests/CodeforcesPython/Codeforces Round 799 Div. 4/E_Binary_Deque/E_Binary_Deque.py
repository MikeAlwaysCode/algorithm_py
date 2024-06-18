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
    n, s = mint()
    nums = ints()
    ans = math.inf
    l = m = 0
    for r, x in enumerate(nums):
        m += x
        while m > s:
            m -= nums[l]
            l += 1
        if m == s:
            ans = min(ans, l + n - 1 - r)

    print(-1 if ans == math.inf else ans)


for _ in range(int(input())):
    solve()

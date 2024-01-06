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
    n = sint()
    nums = ints()
    suff = [0] * n
    for i in range(n - 2, -1, -1):
        suff[i] = max(suff[i + 1], nums[i + 1] + i + 1)
    ans = max(nums[0], suff[0])
    pres = 0
    for i in range(1, n):
        pres = max(pres, nums[i - 1] + n - i)
        ans = min(ans, max(pres, suff[i], nums[i]))
    print(ans)


solve()

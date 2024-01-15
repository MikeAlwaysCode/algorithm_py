import math
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
    n, k, x = mint()
    nums = ints()
    nums.sort()
    pres = list(accumulate(nums, initial=0))
    ans = - math.inf
    for i in range(n, n - k - 1, -1):
        r = max(0, i - x)
        ans = max(ans, pres[r] * 2 - pres[i])
    print(ans)


for _ in range(int(input())):
    solve()

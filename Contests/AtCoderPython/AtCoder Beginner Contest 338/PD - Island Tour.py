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
    n, m = mint()
    d = [0] * (n + 1)
    nums = ints()
    ans, s = math.inf, 0
    for i in range(1, m):
        x, y = nums[i - 1] - 1, nums[i] - 1
        if x > y:
            x, y = y, x
        l1, l2 = y - x, n + x - y
        c = abs(l1 - l2)
        if l1 < l2:
            d[x] += c
            d[y] -= c
        elif l2 < l1:
            d[y] += c
            d[n] -= c
            d[0] += c
            d[x] -= c

        s += min(l1, l2)
    c = 0
    for i in range(n):
        c += d[i]
        ans = min(ans, s + c)
    print(ans)


solve()

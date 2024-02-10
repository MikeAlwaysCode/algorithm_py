import sys
from collections import Counter

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
    n, x = mint()
    nums = ints()
    cnt = Counter(nums)
    for y in cnt.keys():
        z = y ^ x
        if z != y and cnt[z]:
            print("YES")
            return
        if z == y and cnt[y] > 1:
            print("YES")
            return
    print("NO")


solve()

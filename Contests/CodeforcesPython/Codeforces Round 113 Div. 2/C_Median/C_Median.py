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
    n, x = mint()
    nums = ints()
    nums.sort()
    i = bisect_left(nums, x)
    if i == n:
        print(n + 1)
        return
    if nums[i] > x:
        print(min(abs(i * 2 - n), abs(i * 2 + 1 - n), abs(n + 1 - i * 2)) + 1)
        return
    mid = (n - 1) // 2
    j = bisect(nums, x) - 1
    # print(i, j, mid)
    if i <= mid <= j:
        print(0)
    elif i > mid:
        print(i * 2 - n + 1)
    else:
        print(n - j * 2 - 2)


solve()
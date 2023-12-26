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
    nums.sort()
    print(math.comb(nums.count(nums[2]), nums[:3].count(nums[2])))
    '''
    cnt1 = cnt2 = cnt3 = 0
    mn1 = mn2 = mn3 = math.inf
    for x in nums:
        if x * mn2 < mn3:
            cnt3, mn3 = cnt2, x * mn2
        elif x * mn2 == mn3:
            cnt3 += cnt2
        if x * mn1 < mn2:
            cnt2, mn2 = cnt1, x * mn1
        elif x * mn1 == mn2:
            cnt2 += cnt1
        if x < mn1:
            cnt1, mn1 = 1, x
        elif x == mn1:
            cnt1 += 1
    print(cnt3)
    '''


solve()

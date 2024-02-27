import sys
from bisect import *
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
    n = sint()
    nums = ints()
    ans = [-1] * n
    pres = list(accumulate(nums, initial=0))
    left = [-1] * n
    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            left[i] = left[i - 1]
        else:
            left[i] = i - 1
        if nums[i] < nums[i - 1]:
            ans[i] = 1
        elif nums[i] >= pres[i] or left[i - 1] == -1:
            continue
        elif pres[i] - pres[left[i - 1]] > nums[i]:
            ans[i] = i - left[i - 1]
        else:
            k = bisect_left(pres, pres[i] - nums[i])
            ans[i] = i - k + 1
    right = [n] * n
    for i in range(n - 2, -1, -1):
        if nums[i] == nums[i + 1]:
            right[i] = right[i + 1]
        else:
            right[i] = i + 1
        if nums[i] < nums[i + 1]:
            ans[i] = 1
        elif nums[i] >= pres[-1] - pres[i + 1] or right[i + 1] == n:
            continue
        elif pres[right[i + 1] + 1] - pres[i + 1] > nums[i]:
            if ans[i] == -1 or right[i + 1] - i < ans[i]:
                ans[i] = right[i + 1] - i
        else:
            k = bisect(pres, pres[i + 1] + nums[i])
            if ans[i] == -1 or k - i - 1 < ans[i]:
                ans[i] = k - i - 1

    print(*ans)

for _ in range(int(input())):
    solve()

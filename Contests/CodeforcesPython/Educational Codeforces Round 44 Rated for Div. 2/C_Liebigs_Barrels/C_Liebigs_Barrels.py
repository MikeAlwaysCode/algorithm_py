import sys
from bisect import bisect

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
    n, k, l = mint()
    nums = ints()
    nums.sort()
    j = bisect(nums, nums[0] + l)
    if j < n:
        print(0)
        return
    ans = i = 0
    # while n and j - i >= n + k - 1:
    while n and j - i >= n:
        ans += nums[i]
        i += k
        n -= 1
    for _ in range(n):
        j -= 1
        ans += nums[j]
    print(ans)


solve()

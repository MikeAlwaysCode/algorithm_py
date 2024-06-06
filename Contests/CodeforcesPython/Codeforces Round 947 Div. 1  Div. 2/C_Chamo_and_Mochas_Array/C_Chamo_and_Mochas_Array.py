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
    ans = 0
    for i in range(1, n):
        ans = max(ans, min(nums[i], nums[i - 1]))
        if i > 1:
            if nums[i - 1] <= nums[i] <= nums[i - 2]:
                ans = max(ans, nums[i])
            if nums[i - 1] <= nums[i - 2] <= nums[i]:
                ans = max(ans, nums[i - 2])
    print(ans)


for _ in range(int(input())):
    solve()

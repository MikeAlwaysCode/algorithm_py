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
    n, d = mint()
    nums = ints()
    ans = l = 0
    for r, x in enumerate(nums):
        while x - nums[l] > d:
            l += 1
        if r > l + 1:
            ans += (r - l) * (r - l - 1) // 2
    print(ans)

solve()

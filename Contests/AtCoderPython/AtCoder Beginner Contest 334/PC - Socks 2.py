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
    n, k = mint()
    nums = ints()
    ans = sum(nums[i] - nums[i - 1] for i in range(1, k, 2))
    if k & 1:
        suff = sum(nums[i] - nums[i - 1] for i in range(2, k, 2))
        ans = min(ans, suff)
        pref = 0
        for i in range(2, k, 2):
            pref += nums[i - 1] - nums[i - 2]
            suff -= nums[i] - nums[i - 1]
            ans = min(ans, pref + suff)
    print(ans)


solve()

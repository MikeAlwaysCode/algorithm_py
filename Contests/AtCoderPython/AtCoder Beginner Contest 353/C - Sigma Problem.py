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
    n = sint()
    nums = ints()
    nums.sort()
    ans = sum(nums) * (n - 1)
    j = n - 1
    for i in range(n):
        j = max(j, i)
        while j > i and nums[i] + nums[j] >= 10 ** 8:
            j -= 1
        ans -= 10 ** 8 * (n - 1 - j)
    print(ans)

solve()

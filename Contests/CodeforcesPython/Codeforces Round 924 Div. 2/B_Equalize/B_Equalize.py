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
    nums = sorted(ints())
    nums = sorted(set(nums))
    ans = l = 0
    for r in range(len(nums)):
        while nums[r] - nums[l] > n - 1:
            l += 1
        ans = max(ans, r - l + 1)
    print(ans)


for _ in range(int(input())):
    solve()

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
    n, x, y = mint()
    nums = ints()
    nums.sort()

    ans = x - 2
    for i in range(1, x):
        if nums[i] == nums[i - 1] + 2:
            ans += 1
    if nums[0] + n == nums[-1] + 2:
        ans += 1
    print(ans)


for _ in range(int(input())):
    solve()

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
    ans = 0
    while nums[-1] != nums[0]:
        ans += 1
        nums[-1] = (nums[-1] + nums[0]) // 2
    print(ans)
    if 0 < ans <= n:
        print(*[nums[0]] * ans)


for _ in range(int(input())):
    solve()

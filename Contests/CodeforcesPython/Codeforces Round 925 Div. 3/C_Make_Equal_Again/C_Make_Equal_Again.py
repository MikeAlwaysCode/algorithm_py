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
    i, j = 0, n - 1
    while i < n - 1 and nums[i + 1] == nums[i]:
        i += 1
    if i == n - 1:
        print(0)
        return
    while j > 0 and nums[j - 1] == nums[j]:
        j -= 1
    if nums[0] == nums[-1]:
        print(j - i - 1)
    else:
        print(min(n - 1 - i, j))


for _ in range(int(input())):
    solve()

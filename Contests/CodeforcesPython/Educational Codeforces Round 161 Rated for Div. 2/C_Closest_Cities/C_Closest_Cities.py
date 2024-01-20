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
    left, right = [0] * n, [0] * n
    right[1] = 1
    for i in range(2, n):
        if nums[i] - nums[i - 1] < nums[i - 1] - nums[i - 2]:
            right[i] = right[i - 1] + 1
        else:
            right[i] = right[i - 1] + nums[i] - nums[i - 1]
    left[-2] = 1
    for i in range(n - 3, -1, -1):
        if nums[i + 1] - nums[i] < nums[i + 2] - nums[i + 1]:
            left[i] = left[i + 1] + 1
        else:
            left[i] = left[i + 1] + nums[i + 1] - nums[i]

    m = sint()
    for _ in range(m):
        x, y = mint()
        x -= 1
        y -= 1
        if x < y:
            print(right[y] - right[x])
        else:
            print(left[y] - left[x])


for _ in range(int(input())):
    solve()

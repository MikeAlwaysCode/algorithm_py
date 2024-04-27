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
    pos = [-1] * (n + 1)
    for i, x in enumerate(nums, 1):
        pos[x] = i
    ans = []
    for x in range(1, n + 1):
        if pos[x] != x:
            ans.append((x, pos[x]))
            y = nums[x - 1]
            pos[y], pos[x] = pos[x], x
            nums[x - 1], nums[pos[y] - 1] = x, y
    print(len(ans))
    for x, y in ans:
        print(x, y)

solve()

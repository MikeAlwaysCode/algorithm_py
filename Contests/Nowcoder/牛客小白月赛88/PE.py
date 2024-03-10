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
    n, m = mint()
    nums = ints()
    mp = []
    for _ in range(m):
        mp.append(tuple(mint()))
    d = dict()
    for x, y in mp[::-1]:
        if y not in d:
            d[x] = y
        else:
            d[x] = d[y]
    for i, x in enumerate(nums):
        if x in d:
            nums[i] = d[x]
    print(*nums)

for _ in range(sint()):
    solve()

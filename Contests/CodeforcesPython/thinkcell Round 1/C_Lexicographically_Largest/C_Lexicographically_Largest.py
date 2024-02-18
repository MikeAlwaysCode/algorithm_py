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
    ans = []
    idx = sorted(range(n), key = lambda x: -nums[x] - x - 1)
    for i in idx:
        if not ans or ans[-1] > nums[i] + i + 1:
            ans.append(nums[i] + i + 1)
        else:
            ans.append(ans[-1] - 1)

    print(*ans)


for _ in range(int(input())):
    solve()

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
    g = [0] * (n + 1)
    for i, x in enumerate(nums, 1):
        g[i] = i - x

    x = 1
    while g[x] > 0:
        g[x] = -g[x]
        x = -g[x]
    ans = [x]
    x = -g[x]
    while x != ans[0]:
        ans.append(x)
        x = -g[x]
    print(len(ans))
    print(*ans)


for _ in range(int(input())):
    solve()

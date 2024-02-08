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
    nxt = [n] * n
    for i in range(n - 2, -1, -1):
        if nums[i] != nums[i + 1]:
            nxt[i] = i + 1
        else:
            nxt[i] = nxt[i + 1]

    for _ in range(sint()):
        l, r = mint()
        if nxt[l - 1] < r:
            print(l, nxt[l - 1] + 1)
        else:
            print(-1, -1)


for _ in range(int(input())):
    solve()

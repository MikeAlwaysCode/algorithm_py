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
    l, r = mint()
    i, j = 1, l
    ans = []
    while i * j < r:
        while j % 2 == 0 and i * 2 * (j // 2 + 1) <= r:
            j //= 2
            i *= 2
        while i * (j + 1) > r:
            i //= 2
            j *= 2
        ans.append((i * j, i * (j + 1)))
        j += 1
    print(len(ans))
    for s, e in ans:
        print(s, e)


solve()

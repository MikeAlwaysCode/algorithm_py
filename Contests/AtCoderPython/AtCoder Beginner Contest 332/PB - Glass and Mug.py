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
    k, g, m = mint()
    wg = wm = 0
    for i in range(k):
        if wg == g:
            wg = 0
        elif wm == 0:
            wm = m
        else:
            mg = min(g - wg, wm)
            wg += mg
            wm -= mg
    print(wg, wm)


solve()

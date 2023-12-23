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
    a, m, l, r = mint()
    d = abs(l - a)
    k = d // m
    if l <= a:
        l = a - k * m
    elif d % m == 0:
        l = a + k * m
    else:
        l = a + (k + 1) * m
    print(0 if l > r else (r - l) // m + 1)


solve()

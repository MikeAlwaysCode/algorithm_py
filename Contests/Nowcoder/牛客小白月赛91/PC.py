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
    n, m, k = mint()
    x, y = n // 2 + 1, m // 2 + 1
    ans = 0
    for _ in range(k):
        a, b = mint()
        xd, yd = abs(a - x), abs(b - y)
        if (b > xd and m - b >= xd) or (a > yd and n - a >= yd):
            ans += 1
    print(ans)

solve()

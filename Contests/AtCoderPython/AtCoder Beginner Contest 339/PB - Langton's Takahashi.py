import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n, m, k = mint()
    g = [['.'] * m for _ in range(n)]
    x = y = d = 0
    for _ in range(k):
        if g[x][y] == '.':
            g[x][y] = '#'
            d = (d + 1) % 4
        else:
            g[x][y] = '.'
            d = (d - 1) % 4
        x, y = (x + DIR[d][0]) % n, (y + DIR[d][1]) % m
    for row in g:
        print("".join(row))


solve()

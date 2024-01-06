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
    n = sint()
    ans = [[''] * n for _ in range(n)]
    x = y = 0
    d = 1
    v = 1
    while v < n * n:
        ans[x][y] = v
        v += 1
        nx, ny = x + DIR[d][0], y + DIR[d][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or ans[nx][ny] != '':
            d = (d + 1) % 4
            x, y = x + DIR[d][0], y + DIR[d][1]
        else:
            x, y = nx, ny
    ans[x][y] = 'T'
    for row in ans:
        print(*row)


solve()

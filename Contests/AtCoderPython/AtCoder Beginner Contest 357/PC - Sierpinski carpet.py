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
    n = sint()
    m = 3 ** n
    ans = [['.'] * m for _ in range(m)]
    ans[0][0] = '#'
    pp = 1
    for k in range(1, n + 1):
        p = pp * 3
        for i in range(p):
            for j in range(3 ** k):
                if pp <= i < 2 * pp and pp <= j < 2 * pp:
                    continue
                ans[i][j] = ans[i % pp][j % pp]
        pp = p

    for row in ans:
        print(''.join(row))


solve()

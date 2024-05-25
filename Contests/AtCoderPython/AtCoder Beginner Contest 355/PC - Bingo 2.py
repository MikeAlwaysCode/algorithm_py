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
    n, t = mint()
    A = ints()
    row = [0] * n
    col = [0] * n
    dia1 = dia2 = 0
    for i, a in enumerate(A, 1):
        a -= 1
        x, y = divmod(a, n)
        row[x] += 1
        if row[x] == n:
            print(i)
            return
        col[y] += 1
        if col[y] == n:
            print(i)
            return
        if x == y:
            dia1 += 1
            if dia1 == n:
                print(i)
                return
        if x + y == n - 1:
            dia2 += 1
            if dia2 == n:
                print(i)
                return
    print(-1)


solve()

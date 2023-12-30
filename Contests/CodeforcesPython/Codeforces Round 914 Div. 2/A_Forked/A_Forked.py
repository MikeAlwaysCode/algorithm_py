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
    a, b = mint()
    xk, yk = mint()
    xq, yq = mint()
    def zz(x, y) -> int:
        res = 0
        for i in (-1, 1):
            for j in (-1, 1):
                nx, ny = xk + i * x, yk + j * y
                dx, dy = abs(nx - xq), abs(ny - yq)
                if (dx == a and dy == b) or (dx == b and dy == a):
                    res += 1
        return res
    ans = zz(a, b)
    if a != b:
        ans += zz(b, a)
    print(ans)


for _ in range(int(input())):
    solve()

import sys
from functools import cache

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
    n, a, x, y = mint()
    
    @cache
    def f(n: int):
        if n == 0:
            return 0
        res = (y * 6 + sum(f(n // b) for b in range(2, 7))) / 5
        return min(res, x + f(n // a))
    print(f(n))

solve()

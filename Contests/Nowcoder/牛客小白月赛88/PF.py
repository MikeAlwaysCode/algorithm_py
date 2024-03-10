import math
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
    n, m, d = mint()
    g = math.gcd(n, m)
    if g == 1:
        print("YES")
        print(0, 0)
        print("UR")
    elif g == 2:
        print("YES")
        print(0, 1)
        print("UR")
    else:
        print("NO")

solve()

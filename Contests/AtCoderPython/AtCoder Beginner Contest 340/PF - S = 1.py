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

def ext_gcd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, g = ext_gcd(b, a % b)
    x, y = y, x - a // b * y
    return x, y, g

def solve() -> None:
    a, b = mint()
    g = math.gcd(a, b)
    if 2 % g:
        print(-1)
        return
    y, x, g = ext_gcd(a, b)
    x = x * 2 // g
    y = y * 2 // g
    if abs(x * b) > abs(y * a):
        y = -y
    else:
        x = -x
    print(x, y)

solve()

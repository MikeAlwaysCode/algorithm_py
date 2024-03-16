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
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    a, b, c, d = mint()

    ab = a * b
    # gab = math.gcd(a, b) * ab
    k = math.lcm(b+1, ab) // (b+1)
    r = min(c, c // k * k)
    k = math.lcm(d, ab) // d
    l = max(a + 1, a // k * k)
    print("L:", l, "R:", r)
    for i in range(l, r + 1):
        k = math.lcm(i, ab) // i
        cr = (b + k - 1) // k
        if cr * k == b:
            cr += 1
        if cr * k <= d:
            print(i, cr * k)
            return
    print(-1, -1)

for _ in range(int(input())):
    solve()

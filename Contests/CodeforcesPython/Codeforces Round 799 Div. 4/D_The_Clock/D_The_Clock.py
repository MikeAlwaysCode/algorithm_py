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

pal = set()
for t in range(1440):
    h, m = divmod(t, 60)
    h0, h1 = divmod(h, 10)
    m0, m1 = divmod(m, 10)
    if h0 == m1 and h1 == m0:
        pal.add(t)


def solve() -> None:
    s, x = input().split()
    h, m = s.split(':')
    t = int(h) * 60 + int(m)
    g = math.gcd(int(x), 1440)
    ans = 0
    for p in pal:
        if (p - t) % 1440 % g == 0:
            ans += 1
    print(ans)


for _ in range(int(input())):
    solve()

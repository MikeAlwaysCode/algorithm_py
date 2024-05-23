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
    n, m = mint()
    sqn, sqm = math.isqrt(n) + 2, math.isqrt(m) + 2
    bad = [[False] * (sqm + 1) for _ in range(sqn + 1)]
    for i in range(2, min(sqn, sqm) + 1):
        for a in range(i, sqn + 1, i):
            for b in range(i, sqm + 1, i):
                bad[a][b] = True
    ans = 0
    for a in range(1, math.isqrt(n) + 1):
        for b in range(1, math.isqrt(m) + 1):
            if bad[a][b]:
                continue
            ans += min(n // (a + b) // a, m // (a + b) // b)
    print(ans)

for _ in range(int(input())):
    solve()

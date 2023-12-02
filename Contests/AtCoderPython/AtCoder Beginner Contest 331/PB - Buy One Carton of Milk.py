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
    n, s, m, l = mint()
    ans = math.inf
    for i in range((n + 5) // 6 + 1):
        for j in range((n - i * 6 + 7) // 8 + 1):
            ans = min(ans, i * s + j * m + (n - i * 6 - j * 8 + 11) // 12 * l)
    print(ans)

solve()
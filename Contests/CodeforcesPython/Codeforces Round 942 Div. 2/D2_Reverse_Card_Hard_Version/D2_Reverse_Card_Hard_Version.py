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
    ans = 0
    for b in range(2, m + 1):
        r = min(b - 1, m // b)
        l = max(1, b - n // b)
        if r < l:
            break
        # print(b, l, r)
        # ans += max(0, r - l + 1)
        ans += (r - l + 1) * (m // b)

    print(ans)

for _ in range(int(input())):
    solve()

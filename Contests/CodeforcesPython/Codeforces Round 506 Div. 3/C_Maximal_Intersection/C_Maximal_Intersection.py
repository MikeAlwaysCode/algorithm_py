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
    n = sint()
    seg = []
    presl = [-math.inf] * (n + 1)
    presr = [math.inf] * (n + 1)
    for i in range(n):
        seg.append(tuple(mint()))
        presl[i + 1] = max(presl[i], seg[-1][0])
        presr[i + 1] = min(presr[i], seg[-1][1])
    ans = 0
    suffl, suffr = -math.inf, math.inf
    for i in range(n - 1, -1, -1):
        cl, cr = max(presl[i], suffl), min(presr[i], suffr)
        ans = max(ans, cr - cl)
        suffl = max(suffl, seg[i][0])
        suffr = min(suffr, seg[i][1])
    print(ans)

solve()

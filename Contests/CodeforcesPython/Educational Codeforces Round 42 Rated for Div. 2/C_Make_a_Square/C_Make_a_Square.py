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
    s = str(n)
    m = len(s)
    ans = math.inf
    for mask in range(1, 1 << m):
        x = op = 0
        for i in range(m):
            if not (mask >> i) & 1:
                op += 1
                continue
            if x == 0 and s[i] == '0':
                break
            x = x * 10 + int(s[i])
        if x == 0:
            continue
        y = math.isqrt(x)
        if y * y == x:
            ans = min(ans, op)
    print(-1 if ans == math.inf else ans)


solve()

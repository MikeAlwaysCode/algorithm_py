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
    n, m, k = mint()
    ans = math.inf
    g = []
    for _ in range(n):
        g.append(input())
        cnt_x = cnt_o = 0
        for i, c in enumerate(g[-1]):
            if c == 'x':
                cnt_x += 1
            elif c == 'o':
                cnt_o += 1
            if i >= k:
                if g[-1][i - k] == 'x':
                    cnt_x -= 1
                elif g[-1][i - k] == 'o':
                    cnt_o -= 1
            if i >= k - 1 and cnt_x == 0:
                ans = min(ans, k - cnt_o)
    for j in range(m):
        cnt_x = cnt_o = 0
        for i in range(n):
            if g[i][j] == 'x':
                cnt_x += 1
            elif g[i][j] == 'o':
                cnt_o += 1
            if i >= k:
                if g[i - k][j] == 'x':
                    cnt_x -= 1
                elif g[i - k][j] == 'o':
                    cnt_o -= 1
            if i >= k - 1 and cnt_x == 0:
                ans = min(ans, k - cnt_o)

    print(-1 if ans == math.inf else ans)


solve()

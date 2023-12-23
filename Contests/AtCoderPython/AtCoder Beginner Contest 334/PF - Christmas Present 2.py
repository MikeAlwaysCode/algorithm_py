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
    n, k = mint()
    sx, sy = mint()
    d = n % k
    dis = [math.inf] * k
    ans = 0

    def get_dis(x1, y1, x2, y2) -> float:
        return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

    px, py = sx, sy
    for i in range(n):
        x, y = mint()
        ans += get_dis(px, py, x, y)
        if d and i and i % k >= d:
            dis[i % k] = min(dis[i % k], get_dis(px, py, sx, sy) + get_dis(sx, sy, x, y) - get_dis(px, py, x, y))
        px, py = x, y

    ans += get_dis(px, py, sx, sy)
    print(ans)
    print(dis)
    if d:
        ans += min(dis)
    print(ans)


solve()

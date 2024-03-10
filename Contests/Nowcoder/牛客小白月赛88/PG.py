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
    x1, y1, x2, y2, t = mint()
    def calc(p1, p2, p3) -> float:
        a = math.sqrt((p2[0] - p3[0]) * (p2[0] - p3[0]) + (p2[1] - p3[1]) * (p2[1] - p3[1]))
        b = math.sqrt((p1[0] - p3[0]) * (p1[0] - p3[0]) + (p1[1] - p3[1]) * (p1[1] - p3[1]))
        c = math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))
        return math.degrees(math.acos((c * c - a * a - b * b) / (-2 * a * b)))
    
    esp = 10 ** -9
    x3, y3 = x2, y1
    res = calc((x1, y1), (x2, y2), (x3, y3))
    while True:
        if abs(res - t) <= esp:
            break
        if res < t:
            x3 = x2 + (x3 - x2) / 2
        else:
            x3 = x2 + (x3 - x2) * 2
    print(x3, y3)

    
for _ in range(sint()):
    solve()

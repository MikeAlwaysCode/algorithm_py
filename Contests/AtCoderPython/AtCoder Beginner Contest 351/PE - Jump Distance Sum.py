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
    n = sint()
    point = [[] for _ in range(4)]
    for _ in range(n):
        x, y = mint()
        t = (x + y) & 1
        point[t * 2 + 0].append(x + y)
        point[t * 2 + 1].append(x - y)
    ans = 0
    for i in range(4):
        point[i].sort()
        m = len(point[i])
        for j, d in enumerate(point[i]):
            ans += d * (j * 2 + 1 - m)
    print(ans // 2)


solve()

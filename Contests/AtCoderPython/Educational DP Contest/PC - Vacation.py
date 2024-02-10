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
    dp = [0] * 3
    for _ in range(n):
        h = ints()
        tmp = [0] * 3
        for i in range(3):
            tmp[i] = max(dp[(i - 1) % 3], dp[(i + 1) % 3]) + h[i]
        dp = tmp
    print(max(dp))


solve()

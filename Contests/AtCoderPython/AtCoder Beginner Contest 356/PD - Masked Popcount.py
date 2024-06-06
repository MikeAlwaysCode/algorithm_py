import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n, m = mint()
    ans = 0
    for bit in range(60):
        if not (m >> bit) & 1:
            continue
        ans = (ans + (n >> (bit + 1) << bit) + ((n >> bit) & 1) * ((n & ((1 << bit) - 1)) + 1)) % MOD
    print(ans)


solve()

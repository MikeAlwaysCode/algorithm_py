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
    s = input()
    n = int(s)
    m = len(s)
    q = pow(10, m, MOD)
    sn = (pow(q, n, MOD) - 1) * pow(q - 1, MOD - 2, MOD) % MOD
    ans = 0
    for x in map(int, list(s[::-1])):
        ans = (ans + x * sn % MOD) % MOD
        sn = sn * 10 % MOD
    print(ans)


solve()

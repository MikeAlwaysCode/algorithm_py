import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    s = input()
    ans = cnt = 0
    for x in s:
        x = int(x)
        if x & 1:
            cnt = (cnt * 2 + 1) % MOD
        elif x == 0:
            ans = (ans + cnt + 1) % MOD
            cnt = cnt * 2 % MOD
        else:
            ans = (ans + cnt + 1) % MOD
            cnt = (cnt * 2 + 1) % MOD
    print(ans)


solve()

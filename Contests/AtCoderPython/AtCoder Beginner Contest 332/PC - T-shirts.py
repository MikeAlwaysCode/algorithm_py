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
    n, m = mint()
    s = input()
    tot, logt = m, 0
    ct = cl = 0
    for i in range(n - 1, -1, -1):
        if s[i] == '2':
            cl += 1
            ct += 1
        elif s[i] == '1':
            ct += 1
        else:
            logt = max(logt, cl)
            tot = max(tot, ct)
            ct = cl = 0

    logt = max(logt, cl)
    tot = max(tot, ct)
    print(logt + max(0, tot - logt - m))


solve()

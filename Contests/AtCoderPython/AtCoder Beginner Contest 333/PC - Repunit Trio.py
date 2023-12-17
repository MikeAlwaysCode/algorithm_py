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
    rep = []
    x = 1
    for _ in range(12):
        rep.append(x)
        x = x * 10 + 1
    s = []
    for i in range(len(rep)):
        for j in range(i + 1):
            for k in range(j + 1):
                s.append(rep[i] + rep[j] + rep[k])
    # print(s)
    n = sint()
    print(s[n - 1])


solve()

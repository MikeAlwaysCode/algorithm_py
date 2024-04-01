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
    n, q = mint()
    xs = ints()
    ans = [0] * n
    idx = [-1] * n
    pres = [0] * (q + 1)
    s = 0
    for i, x in enumerate(xs, 1):
        pres[i] = pres[i - 1]
        x -= 1
        if idx[x] == -1:
            s += 1
            idx[x] = i - 1
        else:
            s -= 1
            ans[x] += pres[i - 1] - pres[idx[x]]
            idx[x] = -1
        pres[i] += s
    for i in range(n):
        if idx[i] != -1:
            ans[i] += pres[-1] - pres[idx[i]]
    print(*ans)

solve()

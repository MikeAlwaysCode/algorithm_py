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
    n, a, b = mint()
    s = input()
    ans = cnt = l = r = 0
    for c in s:
        cnt += 1 if c == '(' else -1
        if cnt < 0:
            r += 1
            cnt += 2
    l = cnt // 2
    if a < b * 2:
        m = min(l, r)
        ans += m * a
        l -= m
        r -= m
    ans += (l + r) * b
    print(ans)

solve()

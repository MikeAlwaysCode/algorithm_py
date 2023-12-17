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
    s = input()
    t = input()
    d1 = abs(ord(s[0]) - ord(s[1]))
    if d1 > 2:
        d1 = 5 - d1
    d2 = abs(ord(t[0]) - ord(t[1]))
    if d2 > 2:
        d2 = 5 - d2
    print("Yes" if d1 == d2 else "No")


solve()

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
    i, j = -1, len(s)
    while i < len(s) - 1 and s[i + 1] == 'A':
        i += 1
    while j > 0 and s[j - 1] == 'C':
        j -= 1
    print("Yes" if s.count('B') == j - i - 1 else "No")


solve()

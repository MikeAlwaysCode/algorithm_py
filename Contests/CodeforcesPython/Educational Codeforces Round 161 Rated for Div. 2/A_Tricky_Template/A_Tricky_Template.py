import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    A = input()
    B = input()
    C = input()
    ok = 0
    for a, b, c in zip(A, B, C):
        if (a == b and a == c) or (a != b and (a == c or b == c)):
            ok += 1
    print("YES" if ok < n else "NO")


for _ in range(int(input())):
    solve()

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
    s = input()
    A = B = -1
    for i, c in enumerate(s):
        if c == 'A':
            if A == -1:
                A = i
        else:
            B = i
    if A == -1 or B == -1 or A > B:
        print(0)
    else:
        print(B - A)


for _ in range(int(input())):
    solve()

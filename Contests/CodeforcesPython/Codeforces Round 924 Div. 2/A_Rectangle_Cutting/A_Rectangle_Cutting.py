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
    n, m = mint()
    if n & 1 and m & 1:
        print("No")
    elif n & 1:
        print("No" if n * 2 == m else "Yes")
    elif m & 1:
        print("No" if m * 2 == n else "Yes")
    else:
        print("Yes")


for _ in range(int(input())):
    solve()

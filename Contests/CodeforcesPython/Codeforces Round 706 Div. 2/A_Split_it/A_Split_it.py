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
    n, k = mint()
    s = input()
    if k == 0:
        print("YES")
    elif k * 2 + 1 > n:
        print("NO")
    else:
        for i in range(k):
            if s[i] != s[-i-1]:
                print("NO")
                return
        print("YES")


for _ in range(int(input())):
    solve()

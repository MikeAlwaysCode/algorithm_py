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
    k, x, a = mint()
    s = 0
    for _ in range(x):
        if k == 1:
            cur = s + 1
        else:
            cur = (s + k - 1) // (k - 1)
        if a < cur:
            print("NO")
            return
        s += cur
        a -= cur
    print("NO" if a * (k - 1) <= s else "YES")


for _ in range(int(input())):
    solve()

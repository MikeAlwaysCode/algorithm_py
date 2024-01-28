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
    x, n = mint()
    ans = 1
    d = 1
    while d * d <= x:
        if x % d == 0:
            if x // d >= n:
                ans = max(ans, d)
            if d >= n:
                ans = max(ans, x // d)
        d += 1
    print(ans)


for _ in range(int(input())):
    solve()
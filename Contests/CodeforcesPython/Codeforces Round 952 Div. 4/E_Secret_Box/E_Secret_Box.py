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
    x, y, z, k = mint()
    ans = 0
    for a in range(1, x + 1):
        if k % a:
            continue
        for b in range(1, y + 1):
            if k % (a * b):
                continue
            c = k // (a * b)
            if c > z:
                continue
            ans = max(ans, (x - a + 1) * (y - b + 1) * (z - c + 1))
    print(ans)


for _ in range(int(input())):
    solve()

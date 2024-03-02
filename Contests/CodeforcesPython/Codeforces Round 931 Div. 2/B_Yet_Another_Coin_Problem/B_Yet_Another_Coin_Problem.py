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
    a, x = divmod(n, 15)
    b, x = divmod(x, 10)
    c, x = divmod(x, 6)
    d, x = divmod(x, 3)
    if x == 2:
        if a and d:
            a -= 1
            b += 2
            d -= 1
            x -= 2
        elif a and c:
            a -= 1
            c -= 1
            b += 2
            d += 1
            x -= 2
        elif b:
            b -= 1
            c += 2
            x -= 2
    print(a + b + c + d + x)


for _ in range(int(input())):
    solve()

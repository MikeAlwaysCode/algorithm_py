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
    a, b, c = mint()
    z = bin(c)[2:].count('1')
    if z > a + b or (a + b - z) & 1:
        print(-1)
        return
    x = y = 0
    both = (a + b - z) // 2
    cntx = a - both
    for bit in range(60):
        if (c >> bit) & 1:
            if cntx:
                x |= 1 << bit
                cntx -= 1
            else:
                y |= 1 << bit
        elif both:
            x |= 1 << bit
            y |= 1 << bit
            both -= 1
    if both or cntx:
        print(-1)
    else:
        print(x, y)



solve()

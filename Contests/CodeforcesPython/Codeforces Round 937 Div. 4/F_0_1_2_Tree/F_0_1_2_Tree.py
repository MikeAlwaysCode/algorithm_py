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
    a, b, c = mint()

    if c != a + 1:
        print(-1)
        return
    
    if a == 0:
        print(b)
        return

    x, h = 2, 1
    while x < c:
        h += 1
        x <<= 1
    
    if b > x - c:
        h += (b - x + c * 2 - 1) // c
    print(h)


for _ in range(int(input())):
    solve()

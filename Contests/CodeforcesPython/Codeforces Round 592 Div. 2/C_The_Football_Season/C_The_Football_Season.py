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
    n, p, w, d = mint()
    # If y ≥ w, then we can subtract w from y and add d to x, the number of wins and draws will decrease, and the number of points will stay the same.
    for y in range(w):
        q = p - y * d
        if q < 0:
            break
        if q % w == 0 and q // w + y <= n:
            x = q // w
            print(x, y, n - x - y)
            return
    print(-1)

solve()
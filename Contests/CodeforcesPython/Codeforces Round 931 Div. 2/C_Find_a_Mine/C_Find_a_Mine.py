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
    print('?', 1, 1, flush=True)
    d0 = sint()
    print('?', n, m, flush=True)
    d1 = sint()
    # d11 = n + m - d1 - 2
    print('?', 1, m, flush=True)
    d2 = sint()
    x = (d0 + d2 + 3 - m) // 2
    y = d0 + 2 - x
    # if d0 == d11:
    #     print('!', x, y, flush=True)
    # else:
    if x < 1 or x > n or y < 1 or y > m:
        y = (n + m * 2 - 1 - d1 - d2) // 2
        x = d2 + y - m + 1
        print('!', x, y, flush=True)
        return
    print('?', x, y, flush=True)
    d = sint()
    if d == 0:
        print('!', x, y, flush=True)
    else:
        y = (n + m * 2 - 1 - d1 - d2) // 2
        x = d2 + y - m + 1
        print('!', x, y, flush=True)

for _ in range(int(input())):
    solve()

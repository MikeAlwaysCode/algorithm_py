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
    x = sint()
    n = sint()
    c, w = '', 0
    for _ in range(n):
        s = input().split()
        if int(s[1]) > w:
            c, w = s[0], int(s[1])

    ans = c * ((x + w - 1) // w)
    print(ans)
    
solve()

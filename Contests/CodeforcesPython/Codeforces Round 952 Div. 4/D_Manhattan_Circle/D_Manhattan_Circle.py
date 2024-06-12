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
    mn_x, mx_x, mn_y, mx_y = n, 1, m, 1
    for i in range(1, n + 1):
        s = input()
        for j, c in enumerate(s, 1):
            if c == '#':
                mn_x = min(mn_x, i)
                mx_x = max(mx_x, i)
                mn_y = min(mn_y, j)
                mx_y = max(mx_y, j)
    print((mn_x + mx_x) // 2, (mn_y + mx_y) // 2)


for _ in range(int(input())):
    solve()

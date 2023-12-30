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
    g = []
    for _ in range(n):
        g.append(list(input()))

    for i in range(0, n, 3):
        for j in range(m):
            g[i][j] = 'X'
        
        if i + 2 < n:
            if m > 1 and (g[i + 1][1] == 'X' or g[i + 2][1] == 'X'):
                g[i + 1][1] = g[i + 2][1] = 'X'
            else:
                g[i + 1][0] = g[i + 2][0] = 'X'
    
    if n % 3 == 0:
        for j in range(m):
            if g[-1][j] == 'X':
                g[-2][j] = 'X'

    for row in g:
        print("".join(row))


for _ in range(int(input())):
    solve()

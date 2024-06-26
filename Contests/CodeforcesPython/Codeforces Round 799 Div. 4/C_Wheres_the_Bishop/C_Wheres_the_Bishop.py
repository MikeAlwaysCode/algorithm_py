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
    input()
    g = []
    for i in range(8):
        g.append(input())
        
    for i in range(1, 7):
        for j in range(1, 7):
            if g[i][j] == '#' and g[i - 1][j - 1] == '#' and g[i - 1][j + 1] == '#':
                print(i + 1, j + 1)
                return


for _ in range(int(input())):
    solve()

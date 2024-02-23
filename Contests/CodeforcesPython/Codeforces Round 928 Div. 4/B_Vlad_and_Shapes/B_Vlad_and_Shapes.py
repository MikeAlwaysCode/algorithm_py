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
    g = []
    for _ in range(n):
        g.append(input())
 
    for i in range(n):
        for j in range(n):
            if g[i][j] == '1':
                if i + 1 < n and g[i + 1][j] == '1' and j + 1 < n and g[i][j + 1]  == '1':
                    print("SQUARE")
                else:
                    print("TRIANGLE")
                return


for _ in range(int(input())):
    solve()

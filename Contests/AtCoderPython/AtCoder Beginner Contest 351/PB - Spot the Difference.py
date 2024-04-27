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
    n = sint()
    g1 = []
    for _ in range(n):
        g1.append(input())
    g2 = []
    for _ in range(n):
        g2.append(input())
    
    for i in range(n):
        for j in range(n):
            if g1[i][j] != g2[i][j]:
                print(i + 1, j + 1)
                return

solve()

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
    dia1, dia2 = [0] * (n + m), [0] * (n + m)
    for i in range(n):
        g.append(ints())
        for j, x in enumerate(g[i]):
            dia1[i - j + m] += x
            dia2[i + j] += x
    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(ans, dia1[i - j + m] + dia2[i + j] - g[i][j])
    print(ans)


for _ in range(int(input())):
    solve()

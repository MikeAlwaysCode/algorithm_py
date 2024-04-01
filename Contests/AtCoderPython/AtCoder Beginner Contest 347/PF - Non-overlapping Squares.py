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
    n, m = mint()
    mat = []
    for _ in range(n):
        mat.append(ints())

    prefix = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1]

    def getRect(x1, y1, x2, y2) -> int:
            return prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]
    
    g10 = [[0] * (n + 2) for _ in range(n + 2)]
    g11 = [[0] * (n + 2) for _ in range(n + 2)]
    gr = [0] * (n + 2)
    gc = [0] * (n + 2)

    for i in range(m, n + 1):
         for j in range(n - m + 1, 0, -1):
              s = getRect(i - m + 1, j, i, j + m - 1)
              g11[i][j] = max(s, g11[i - 1][j], g11[i][j + 1])
              
         for j in range(m, n + 1):
              s = getRect(i - m + 1, j - m + 1, i, j)
              g10[i][j] = max(s, g10[i - 1][j], g10[i][j - 1])

              gr[i] = max(gr[i], max(g10[i - m][j], g10[i][j - m], g11[i][j + 1]) + s)
              gc[j] = max(gc[j], max(g10[i - m][j], g10[i][j - m]) + s)
              gc[j] = max(gc[j], gc[j - 1])
    
    # print(g10)
    # print(gr)

    f10 = [[0] * (n + 2) for _ in range(n + 2)]
    f11 = [[0] * (n + 2) for _ in range(n + 2)]
    fr = [0] * (n + 2)
    fc = [0] * (n + 2)

    for i in range(n - m + 1, 0, -1):
         for j in range(m, n + 1):
              s = getRect(i, j - m + 1, i + m - 1, j)
              f11[i][j] = max(s, f11[i + 1][j], f11[i][j - 1])

         for j in range(n - m + 1, 0, -1):
              s = getRect(i, j, i + m - 1, j + m - 1)
              f10[i][j] = max(s, f10[i + 1][j], f10[i][j + 1])

              fr[i] = max(fr[i], max(f10[i + m][j], f10[i][j + m], f11[i][j - 1]) + s)
              fc[j] = max(fc[j], f10[i + m][j], f10[i][j + m] + s)
              fc[j] = max(fc[j], fc[j + 1])
    
    ans = 0
    for i in range(m, n + 1):
         for j in range(m, n + 1):
              s = getRect(i - m + 1, j - m + 1, i, j)
              ans = max(ans, s + gr[i - m], s + gc[j - m], s + fr[i + 1], s + fc[j + 1])
    
    print(ans)


solve()

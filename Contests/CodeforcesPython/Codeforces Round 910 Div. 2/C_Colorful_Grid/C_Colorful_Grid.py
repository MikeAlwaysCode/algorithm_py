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
    n, m, k = mint()
    s = n + m - 2
    if k < s or (k - s) & 1:
        print("NO")
        return
    row = [['R'] * (m - 1) for _ in range(n)]
    col = [['B'] * m for _ in range(n - 1)]
    if n > m + 1:
        for i in range(n - m - 2, -1, -1):
            if col[i + 1][0] == 'B':
                col[i][0] = 'R'
            else:
                col[i][0] = 'B'
    if n < m:
        for i in range(m - n - 1, -1, -1):
            if row[0][i + 1] == 'B':
                row[0][i] = 'R'
            else:
                row[0][i] = 'B'
    if (k - s) % 4 == 2:
        row[-1][-1] = 'B'
    print("YES")
    for s in row:
        print(*s)
    for s in col:
        print(*s)

for _ in range(int(input())):
    solve()
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
    A = []
    for _ in range(n):
        A.append(ints())
    B = []
    for _ in range(n):
        B.append(ints())
    ax = ay = -1
    bx = by = -1
    for i in range(n):
        for j in range(m):
            if A[i][j] == 1:
                ax, ay = i, j
            if B[i][j] == 1:
                bx, by = i, j
    col_a = sorted(range(m), key = lambda x: A[ax][x])
    col_b = sorted(range(m), key = lambda x: B[bx][x])
    row_a = sorted(range(n), key = lambda x: A[x][ay])
    row_b = sorted(range(n), key = lambda x: B[x][by])
    for i in range(n):
        for j in range(m):
            if A[row_a[i]][col_a[j]] != B[row_b[i]][col_b[j]]:
                print("NO")
                return
    print("YES")


for _ in range(int(input())):
    solve()

INF = 2 * 10**9

def solve() -> None:
    m = int(input())
    a = [[int(x) for x in input().split()] for i in range(2)]
    su = [[-INF for j in range(m + 1)] for i in range(2)]

    for i in range(2):
        for j in range(m - 1, -1, -1):
            su[i][j] = max(su[i][j + 1] - 1, a[i][j], a[i ^ 1][j] - (2 * (m - j) - 1))

    pr = a[0][0] - 1
    ans = INF
    for j in range(m):
        jj = j & 1
        ans = min(ans, max(pr, su[jj][j + 1] - 2 * j - 1, a[jj ^ 1][j] - 2 * m + 1))
        pr = max(pr, a[jj ^ 1][j] - 2 * j - 1)
        ans = min(ans, max(pr, su[jj ^ 1][j + 1] - 2 * j - 2))
        if j < m - 1:
            pr = max(pr, a[jj ^ 1][j + 1] - 2 * j - 2)
    print(ans + 2 * m)

t = int(input())
for _ in range(t):
    solve()
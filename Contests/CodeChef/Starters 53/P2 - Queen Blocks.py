from collections import Counter, defaultdict

def solve() -> None:
    a, b = map(int, input().split())
    ans = [[0] * 8 for _ in range(8)]

    a -= 1
    b -= 1
    ans[a][b] = 1

    if a == 0 and b == 0:
        ans[1][2] = 2
    elif a == 0 and b == 7:
        ans[1][5] = 2
    elif a == 7 and b == 0:
        ans[6][2] = 2
    elif a == 7 and b == 7:
        ans[6][5] = 2
    elif a == 0:
        ans[2][b-1] = 2
        ans[2][b+1] = 2
    elif a == 7:
        ans[5][b-1] = 2
        ans[5][b+1] = 2
    elif b == 0:
        ans[a-1][2] = 2
        ans[a+1][2] = 2
    elif b == 7:
        ans[a-1][5] = 2
        ans[a+1][5] = 2
    else:
        dir = [(-3, -1, 1, 2), (-2, -1, 1, 3), (-3, 1, 1, -2), (-2, 1, 1, -3), (-1, 3, 2, -1), (-1, 2, 3, -1), (2, 1, -1, -3), (3, 1, -1, -2)]
        for i1, j1, i2, j2 in dir:
            ni1 = a + i1
            nj1 = b + j1
            ni2 = a + i2
            nj2 = b + j2
            if 0 <= ni1 < 8 and 0 <= nj1 < 8 and 0 <= ni2 < 8 and 0 <= nj2 < 8:
                ans[ni1][nj1] = 2
                ans[ni2][nj2] = 2
                break

    for row in ans:
        print(*row)

t = int(input())
for _ in range(t):
    solve()
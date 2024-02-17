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
    n, m, k = mint()
    s = input()
    g = []
    for _ in range(n):
        g.append(input())
    
    def check(x, y) -> int:
        i = 0
        while i < k and 0 <= x < n and 0 <= y < m and g[x][y] == '.':
            if s[i] == 'L':
                y -= 1
            elif s[i] == 'R':
                y += 1
            elif s[i] == 'U':
                x -= 1
            else:
                x += 1
            i += 1
        if i == k and 0 <= x < n and 0 <= y < m and g[x][y] == '.':
            return 1
        else:
            return 0

    ans = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if g[i][j] == '.':
                ans += check(i, j)
    print(ans)

solve()

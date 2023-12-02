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
    n, q = mint()
    mat = [[0] * n for _ in range(n)]
    for i in range(n):
        s = input()
        for j, c in enumerate(s):
            if c == 'B':
                mat[i][j] = 1
    
    prefix = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1]
    
    def zz(x1, y1, x2, y2) -> int:
        return prefix[x2 + 1][y2 + 1] - prefix[x1][y2 + 1] - prefix[x2 + 1][y1] + prefix[x1][y1]
    
    def zz2(x, y) -> int:
        k1, k2 = x // n, y // n
        res = k1 * k2 * prefix[-1][-1] + zz(0, 0, x % n, y % n)
        if k1:
            res += k1 * zz(0, 0, n - 1, y % n)
        if k2:
            res += k2 * zz(0, 0, x % n, n - 1)
        return res

    for _ in range(q):
        a, b, c, d = mint()
        ans = zz2(c, d)
        if a:
            ans -= zz2(a - 1, d)
        if b:
            ans -= zz2(c, b - 1)
        if a and b:
            ans += zz2(a - 1, b - 1)

        print(ans)

solve()
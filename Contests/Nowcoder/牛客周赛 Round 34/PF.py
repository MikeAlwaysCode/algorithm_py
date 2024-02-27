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

def ext_gcd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, g = ext_gcd(b, a % b)
    x, y = y, x - a // b * y
    return x, y, g

def solve() -> None:
    n, m, x = mint()
    if x == 2:
        print(-1)
        return
    ans = [[0] * m for _ in range(n)]
    if x % 4 == 0:
        ans[0][0] = ans[0][1] = ans[1][0] = ans[1][1] = x // 4
    else:
        ans[0][0] = ans[0][1] = ans[1][1] = ans[1][2] = ans[2][0] = ans[2][2] = 1
        ans[0][2] = ans[0][3] = ans[-1][2] = ans[-1][3] = (x - 6) // 4
    
    for i in range(n):
        print(*ans[i])


solve()

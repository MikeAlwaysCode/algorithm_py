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
    n = sint()
    p = ints()

    sz = [1] * n
    dp = [1.0] * n
    for i in range(n - 1, 0, -1):
        sz[p[i - 1] - 1] += sz[i]
    
    for i in range(1, n):
        dp[i] = dp[p[i - 1] - 1] + (sz[p[i - 1] - 1] - sz[i] - 1) / 2 + 1
    
    print(*dp)

solve()

import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n, m, k = mint()
    p = 0
    for _ in range(m):
        a, b, f = mint()
        p += f
    ans = 0
    q0 = q = n * (n - 1) // 2
    ans = p * pow(q, MOD - 2, MOD) % MOD
    more = m
    for _ in range(k - 1):
        p = p * q + more
        q0 = q0 * q % MOD
        ans = (ans + p * pow(q0, MOD - 2, MOD)) % MOD
        more = more * q
    print(ans)


for _ in range(int(input())):
    solve()
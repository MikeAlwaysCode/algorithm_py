import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

n = 10 ** 6
# 阶乘
fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = fact[i-1] * i % MOD
# 逆元
inverse = [0] * (n + 1)
inverse[n] = pow(fact[n], MOD - 2, MOD)
for i in range(n, 0, -1):
    inverse[i-1] = inverse[i] * i % MOD
# 组合数
def comb(n: int, m: int, MOD = MOD) -> int:
    if m < 0 or m > n:
        return 0
    return fact[n] * inverse[m] % MOD * inverse[n-m] % MOD

def solve() -> None:
    m, a, b, c = mint()

    p3 = m
    p2 = 3 * m * (m - 1) % MOD
    p1 = 6 * comb(m, 3) % MOD
    q = pow(m, 3, MOD)
    ans = (p3 * c + p2 * b + p1 * a) % MOD * pow(q, MOD - 2, MOD) % MOD
    print(ans)

for _ in range(sint()):
    solve()

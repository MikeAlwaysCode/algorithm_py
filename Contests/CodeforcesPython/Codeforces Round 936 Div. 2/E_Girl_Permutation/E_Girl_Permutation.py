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

mx = 2 * 10 ** 5
# 阶乘
fact = [1] * (mx + 1)
for i in range(1, mx + 1):
    fact[i] = fact[i-1] * i % MOD
# 逆元
inverse = [0] * (mx + 1)
inverse[mx] = pow(fact[mx], MOD - 2, MOD)
for i in range(mx, 0, -1):
    inverse[i-1] = inverse[i] * i % MOD
# 组合数
def comb(n: int, m: int, MOD = MOD) -> int:
    if m < 0 or m > n:
        return 0
    return fact[n] * inverse[m] % MOD * inverse[n-m] % MOD

def solve() -> None:
    n, m1, m2 = mint()
    pres = ints()
    suff = ints()
    if pres[-1] != suff[0] or pres[0] != 1 or suff[-1] != n:
        print(0)
        return
    ans = comb(n - 1, n - suff[0])
    s = n - suff[0]
    for i in range(1, m2):
        s -= 1
        k = suff[i] - suff[i - 1] - 1
        if k:
            ans *= comb(s, k) * fact[k]
            ans %= MOD
            s -= k
    s = suff[0] - 1
    for i in range(m1 - 2, -1, -1):
        s -= 1
        k = pres[i + 1] - pres[i] - 1
        if k:
            ans *= comb(s, k) * fact[k]
            ans %= MOD
            s -= k
    print(ans)

for _ in range(int(input())):
    solve()

import sys
from functools import cache

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

mx = 2 * 10 ** 6
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
    c1, c2, c3, c4 = mint()

    if c1 - c2 > 1 or c2 - c1 > 1:
        print(0)
        return
    
    if c1 == c2 == 0:
        print(0 if c3 != 0 and c4 != 0 else 1)
        return

    ans = 1
    if c1 > c2:
        ans *= comb(c3 + c1 - 1, c1 - 1)
        ans = ans * comb(c4 + c1 - 1, c1 - 1) % MOD
    elif c2 > c1:
        ans *= comb(c3 + c2 - 1, c2 - 1)
        ans = ans * comb(c4 + c2 - 1, c2 - 1) % MOD
    if c1 == c2:
        ans = comb(c3 + c1, c1) * comb(c4 + c2 - 1, c2 - 1) % MOD
        ans = (ans + comb(c3 + c1 - 1, c1 - 1) * comb(c4 + c2, c2) % MOD) % MOD

    print(ans)


for _ in range(int(input())):
    solve()

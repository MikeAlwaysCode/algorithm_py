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

mx = 3 * 10 ** 5
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
    n, k = mint()
    seen = [True] * n
    for _ in range(k):
        x, y = mint()
        seen[x - 1] = seen[y - 1] = False
    cnt = sum(v for v in seen)
    ans = 0
    for i in range(cnt & 1, cnt + 1, 2):
        res = comb(cnt - i, (cnt - i) // 2) * fact[(cnt - i) // 2] % MOD
        res = res * comb(cnt, i)
        ans = (ans + res) % MOD
    print(ans)


for _ in range(int(input())):
    solve()

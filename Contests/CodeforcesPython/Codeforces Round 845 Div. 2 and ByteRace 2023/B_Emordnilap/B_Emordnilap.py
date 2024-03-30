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

# 阶乘
mx = 10 ** 5
fact = [1] * (mx + 1)
for i in range(1, mx + 1):
    fact[i] = fact[i-1] * i % MOD


def solve() -> None:
    n = sint()
    ans = (n - 1) * n * fact[n] % MOD
    print(ans)


for _ in range(int(input())):
    solve()

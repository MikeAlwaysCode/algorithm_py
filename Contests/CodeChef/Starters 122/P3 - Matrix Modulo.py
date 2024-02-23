import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# MOD = 998_244_353
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

mx = 250000
# 阶乘
fact = [1] * (mx + 1)
for i in range(1, mx + 1):
    fact[i] = fact[i-1] * i % MOD

def solve() -> None:
    n = sint()
    g = []
    for _ in range(n):
        g.append(ints())
    x = n * (n - 1) // 2
    l, r = x + 1, x + n
    dia = cnt = 0
    s = set()
    for i in range(n):
        if g[i][i] == 0:
            dia += 1
        elif g[i][i] < l or g[i][i] > r:
            print(0)
            return
        for j in range(i + 1, n):
            a, b = g[i][j], g[j][i]
            if a == 0 and b == 0:
                cnt += 1
                continue
            if a != 0 and (l <= a <= r or a + r in s or a - r in s):
                print(0)
                return
            if b != 0 and (l <= b <= r or b + r in s or b - r in s):
                print(0)
                return
            if a != 0 and b != 0 and abs(a - b) != r:
                print(0)
                return
            if a != 0:
                s.add(a)
            if b != 0:
                s.add(b)

    ans = fact[dia] * fact[cnt] % MOD * pow(2, cnt, MOD) % MOD
    print(ans)


for _ in range(sint()):
    solve()

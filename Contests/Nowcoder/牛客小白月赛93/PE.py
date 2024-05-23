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

def solve() -> None:
    n, m = mint()
    s = input()
    cnt = [[0] * 2 for _ in range(n + 1)]
    d = [[0] * 2 for _ in range(n + 1)]
    pres = [0] * (n + 1)
    for i, c in enumerate(s):
        cnt[i + 1] = cnt[i][:]
        d[i + 1] = d[i][:]

        c = int(c)
        cnt[i + 1][c] += 1
        d[i + 1][c] += i
        pres[i + 1] = (pres[i] + i * cnt[i][c ^ 1] - d[i][c ^ 1]) % MOD
    
    for _ in range(m):
        l, r = mint()
        ans = (pres[r] - pres[l - 1]) % MOD
        for c in range(2):
            ans = (ans - (d[r][c] - d[l - 1][c]) * cnt[l - 1][c ^ 1] + d[l - 1][c ^ 1] * (cnt[r][c] - cnt[l - 1][c])) % MOD
        print(ans)

solve()

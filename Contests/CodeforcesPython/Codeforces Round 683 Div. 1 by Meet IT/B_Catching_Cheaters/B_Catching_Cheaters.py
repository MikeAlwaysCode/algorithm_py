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
    n, m = mint()
    s = input()
    t = input()
    f = [0] * (m + 1)
    g = [0] * (m + 1)
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                g[j + 1] = max(2, f[j] + 2)
                if g[j + 1] > ans:
                    ans = g[j + 1]
            else:
                g[j + 1] = max(f[j + 1], g[j]) - 1

        f, g = g, f

    print(ans)

solve()
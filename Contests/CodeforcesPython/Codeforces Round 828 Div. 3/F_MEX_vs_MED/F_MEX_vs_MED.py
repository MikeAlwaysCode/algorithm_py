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
    l, r = n, -1
    d = {v:i for i, v in enumerate(p)}
    ans = 0
    for m in range(1, n + 1):
        i = d[(m - 1) // 2]
        l = min(l, i, n - m)
        r = max(r, i)
        ans += max(0, min(m - r + l, l + 1, n - r))
    print(ans)

for _ in range(int(input())):
    solve()

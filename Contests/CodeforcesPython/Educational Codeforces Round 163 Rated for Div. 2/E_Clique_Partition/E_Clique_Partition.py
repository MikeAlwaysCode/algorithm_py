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
    n, k = mint()
    a = []
    c = []
    q = 0
    for l in range(1, n + 1, k):
        r = min(n, l + k - 1)
        q += 1
        c.extend([q] * (r - l + 1))
        mid = (l + r) // 2
        a.extend(range(mid, r + 1))
        a.extend(range(l, mid))

    print(*a)
    print(q)
    print(*c)


for _ in range(int(input())):
    solve()

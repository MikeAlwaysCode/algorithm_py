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
    n, p, l, t = mint()
    task = (n + 6) // 7
    ans = min(task // 2, (p + l + t * 2 - 1) // (l + t * 2))
    p -= ans * (l + t * 2)
    if p <= 0:
        print(n - ans)
        return
    if task & 1:
        ans += 1
        p -= l + t
    if p > 0:
        ans += (p + l - 1) // l
    print(n - ans)

for _ in range(int(input())):
    solve()
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
    l = r = m
    pre = 0
    ans = True
    for _ in range(n):
        t, L, R = mint()
        if not ans:
            continue
        l = max(L, l - t + pre)
        r = min(R, r + t - pre)
        if l > r:
            ans = False
        pre = t
    
    print("YES" if ans else "NO")


for _ in range(int(input())):
    solve()

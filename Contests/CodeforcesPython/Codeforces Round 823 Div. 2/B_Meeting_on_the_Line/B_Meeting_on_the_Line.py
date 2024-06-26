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
    n = int(input())
    arrx = ints()
    arrt = ints()

    mn = 10 ** 8
    mx = 0
    for i in range(n):
        mn = min(mn, arrx[i] - arrt[i])
        mx = max(mx, arrx[i] + arrt[i])
    
    ans = (mn + mx) / 2
    print(f"{ans:.6f}")


for _ in range(int(input())):
    solve()
    
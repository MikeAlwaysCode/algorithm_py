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
    n, m, k = mint()

    def check(x: int) -> bool:
        l1, l2 = min(x, k), min(x, n - k + 1)
        res = (x + max(1, x - k + 1)) * l1 // 2 + (x + max(1, x - n + k)) * l2 // 2 - x + n - l1 - l2 + 1
        return res <= m

    l, r = 1, m
    while l < r:
        mid = (l + r + 1) // 2
        if check(mid):
            l = mid
        else:
            r = mid - 1
    print(l)


solve()

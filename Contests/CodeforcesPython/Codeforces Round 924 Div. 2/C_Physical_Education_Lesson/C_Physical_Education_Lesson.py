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
    n, x = mint()
    ans = set()
    m = n - x
    if not m & 1:
        d = 1
        while d * d <= m:
            if m % d == 0:
                if not d & 1 and d // 2 + 1 >= x:
                    ans.add(d // 2 + 1)
                dd = m // d
                if not dd & 1 and dd // 2 + 1 >= x:
                    ans.add(dd // 2 + 1)
            d += 1
    m = n + x - 2
    if not m & 1:
        d = 1
        while d * d <= m:
            if m % d == 0:
                if not d & 1 and d // 2 + 1 >= x:
                    ans.add(d // 2 + 1)
                dd = m // d
                if not dd & 1 and dd // 2 + 1 >= x:
                    ans.add(dd // 2 + 1)
            d += 1
    print(len(ans))

for _ in range(int(input())):
    solve()

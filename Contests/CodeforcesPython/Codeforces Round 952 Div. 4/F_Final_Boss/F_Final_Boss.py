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
    h, n = mint()
    A = ints()
    C = ints()
    s = sum(A)

    def check(x: int) -> bool:
        res = 0
        for a, c in zip(A, C):
            res += ((x - 1) // c + 1) * a
        return res >= h
    
    l, r = 1, ((h + s - 1) // s - 1) * max(C) + 1
    while l < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid + 1
    print(r)


for _ in range(int(input())):
    solve()

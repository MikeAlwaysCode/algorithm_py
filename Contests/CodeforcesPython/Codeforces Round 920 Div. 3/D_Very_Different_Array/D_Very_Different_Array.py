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
    A = ints()
    B = ints()
    A.sort()
    B.sort()
    ans = 0
    ai, aj, bi, bj = 0, n - 1, 0, m - 1
    while ai <= aj:
        if abs(A[ai] - B[bj]) >= abs(A[aj] - B[bi]):
            ans += abs(A[ai] - B[bj])
            ai += 1
            bj -= 1
        else:
            ans += abs(A[aj] - B[bi])
            aj -= 1
            bi += 1
    print(ans)


for _ in range(int(input())):
    solve()

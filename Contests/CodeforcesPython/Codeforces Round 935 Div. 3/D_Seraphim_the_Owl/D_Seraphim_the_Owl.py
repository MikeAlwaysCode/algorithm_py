import math
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
    ans, suff = math.inf, 0
    for i in range(n - 1, -1, -1):
        if i < m:
            ans = min(ans, A[i] + suff)
        suff += min(A[i], B[i])
    print(ans)


for _ in range(int(input())):
    solve()

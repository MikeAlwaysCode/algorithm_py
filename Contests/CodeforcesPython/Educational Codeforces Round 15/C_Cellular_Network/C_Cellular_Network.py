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
    ans = j = 0
    for i in range(n):
        while j < m and B[j] < A[i]:
            j += 1
        res = math.inf if j >= m else B[j] - A[i]
        if j:
            res = min(res, A[i] - B[j - 1])
        ans = max(ans, res)
    print(ans)


solve()

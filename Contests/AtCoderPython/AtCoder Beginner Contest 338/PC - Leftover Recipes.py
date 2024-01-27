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
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    q = ints()
    A = ints()
    B = ints()
    mx = math.inf
    for i in range(n):
        if A[i]:
            mx = min(mx, q[i] // A[i])
    ans = mx
    for i in range(mx + 1):
        mxb = math.inf
        for j in range(n):
            if B[j]:
                mxb = min(mxb, (q[j] - i * A[j]) // B[j])
        ans = max(ans, i + mxb)
    print(ans)

solve()

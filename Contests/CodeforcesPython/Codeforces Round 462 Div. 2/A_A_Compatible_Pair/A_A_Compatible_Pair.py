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
    res1 = max(A[1] * B[0], A[1] * B[-1], A[-1] * B[0], A[-1] * B[-1])
    res2 = max(A[0] * B[0], A[0] * B[-1], A[-2] * B[0], A[-2] * B[-1])
    print(min(res1, res2))

solve()

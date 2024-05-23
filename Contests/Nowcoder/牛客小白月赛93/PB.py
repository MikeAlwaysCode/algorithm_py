import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    A = list(map(int, list(input())))
    B = list(map(int, list(input())))
    for i, (a, b) in enumerate(zip(A, B)):
        if a > b:
            A[i], B[i] = B[i], A[i]
    sa = sb = 0
    for a, b in zip(A, B):
        sa = (sa * 10 + a) % MOD
        sb = (sb * 10 + b) % MOD
    print(sa * sb % MOD)

solve()

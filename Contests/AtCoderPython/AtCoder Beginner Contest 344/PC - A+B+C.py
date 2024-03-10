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
    A = ints()
    m = sint()
    B = ints()
    l = sint()
    C = ints()

    s = set()
    for i in range(n):
        for j in range(m):
            for k in range(l):
                s.add(A[i] + B[j] + C[k])

    q = sint()
    qry = ints()
    for x in qry:
        print("Yes" if x in s else "No")


solve()

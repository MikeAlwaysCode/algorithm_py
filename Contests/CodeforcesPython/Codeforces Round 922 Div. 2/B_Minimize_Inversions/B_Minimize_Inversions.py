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
    n = sint()
    A = ints()
    B = ints()
    idx = sorted(range(n), key = lambda x: A[x])
    ansa, ansb = [], []
    for i in idx:
        ansa.append(A[i])
        ansb.append(B[i])
    print(*ansa)
    print(*ansb)


for _ in range(int(input())):
    solve()

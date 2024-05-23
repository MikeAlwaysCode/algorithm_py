import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

def solve() -> None:
    n = sint()
    A = ints()
    B = ints()
    idx = sorted(range(n), key = lambda x: A[x] * (x + 1) * (n - x))
    B.sort(reverse=True)
    ans = 0
    for i, j in enumerate(idx):
        ans = (ans + B[i] * A[j] * (j + 1) * (n - j) % MOD) % MOD
    print(ans)


solve()

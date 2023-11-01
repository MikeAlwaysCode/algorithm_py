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
    ans = s = sum(B)
    idx = sorted(range(n), key = lambda x: A[x])
    for i in idx:
        s -= B[i]
        ans = min(ans, max(A[i], s))
    print(ans)

for _ in range(int(input())):
    solve()
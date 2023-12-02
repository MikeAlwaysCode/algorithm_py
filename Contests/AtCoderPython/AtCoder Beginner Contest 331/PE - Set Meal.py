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
    n, m, l = mint()
    A = ints()
    B = ints()
    ans = 0
    f = set(range(m))
    idx = sorted(range(n), key = lambda x: - A[x])
    exc = [set() for _ in range(n)]
    for _ in range(l):
        a, b = mint()
        a -= 1
        b -= 1
        exc[a].add(b)
    for i in idx:
        g = set()
        for j in f:
            if j in exc[i]:
                g.add(j)
            else:
                ans = max(ans, A[i] + B[j])
        if not g:
            break
        f = g
    print(ans)

solve()
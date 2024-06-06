import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

def solve() -> None:
    n, q = mint()
    V = ints()
    C = ints()
    m = max(C)
    inf = pow(10, 15) + 1
    f = [-inf] * (m + 1)
    ans = []
    for _ in range(q):
        a, b = mint()
        f[0] = 0
        for i in range(1, m + 1):
            f[i] = -inf
        i = j = 0
        for v, c in zip(V, C):
            x = f[c] + v * a
            y = f[i] + v * b if i ^ c else f[j] + v * b
            if x < y:
                x = y
            if f[c] < x:
                f[c] = x
                if f[i] < x:
                    i, j = c, i
                elif i ^ c and f[j] < x:
                    j = c
        ans.append(f[i])
    print(*ans, sep='\n')

solve()

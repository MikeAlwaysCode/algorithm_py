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
    n, m = mint()
    fa = list(range(n + 1))
    sz = [1] * (n + 1)
    edges = [0] * (n + 1)
    def find(x: int):
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            fa[cur], cur = x, fa[cur]
        return x
    for _ in range(m):
        u, v = mint()
        fu, fv = find(u), find(v)
        if fu != fv:
            fa[fv] = fu
            sz[fu] += sz[fv]
            edges[fu] += edges[fv]
        edges[fu] += 1
    ans = 0
    for i in range(1, n + 1):
        if find(i) == i:
            ans += sz[i] * (sz[i] - 1) // 2 - edges[i]
    print(ans)

solve()

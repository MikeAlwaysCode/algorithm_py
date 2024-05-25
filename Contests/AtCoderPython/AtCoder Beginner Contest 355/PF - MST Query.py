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
    n, q = mint()
    edges = []
    for _ in range(n - 1):
        u, v, w = mint()
        u -= 1
        v -= 1
        edges.append((w, u, v))

    fa = [list(range(n + 1))]
    
    def find(x: int, k: int):
        cur = x
        while x != fa[k][x]:
            x = fa[k][x]
        while fa[k][cur] != x:
            fa[k][cur], cur = x, fa[k][cur]
        return x

    edges.sort()
    ans = k = 0
    for w, u, v in edges:
        ans += w
        u = find(u, k)
        v = find(v, k)
        while w > k:
            fa.append(fa[-1][:])
            k += 1
        fa[k][u] = v
    
    for _ in range(q):
        u, v, w = mint()
        u -= 1
        v -= 1
        k = 1
        while find(u, k) != find(v, k):
            k += 1
        # print(k)
        if k > w:
            ans += w - k
            for k in range(w, len(fa)):
                fu, fv = find(u, k), find(v, k)
                fa[k][fu] = fv
        print(ans)


solve()

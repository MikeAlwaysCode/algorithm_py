import sys

# region fastio
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

MOD = 998_244_353
BASE = 27
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def solve() -> None:
    n = sint()
    v = input()
    m = n.bit_length()
    pa = [[-1] * (n + 1) for _ in range(m)]
    pa[0] = [-1] + ints()
    
    depth = [0] * (n + 1)
    hash1 = [0] * (n + 1)
    hash2 = [0] * (n + 1)
    for i in range(1, n + 1):
        d = ord(v[i - 1]) - 96
        # if (p := pa[0][i]) != -1:
        p = pa[0][i]
        depth[i] = depth[p] + 1
        hash1[i] = (hash1[p] * BASE + d) % MOD
        hash2[i] = (hash2[p] + d * pow(BASE, depth[i] - 1, MOD)) % MOD

    for i in range(m - 1):
        for x in range(1, n + 1):
            # if (p := pa[i][x]) != -1:
            p = pa[i][x]
            if p != -1:
                pa[i + 1][x] = pa[i][p]

    def get_kth_ancestor(node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if (k >> i) & 1:
                node = pa[i][node]
        return node

    def get_lca(x: int, y: int) -> int:
        if depth[x] > depth[y]:
            x, y = y, x
        y = get_kth_ancestor(y, depth[y] - depth[x])
        if y == x:
            return x
        for i in range(m - 1, -1, -1):
            px, py = pa[i][x], pa[i][y]
            if px != py:
                x, y = px, py
        return pa[0][x]
    
    def get_hash1(u: int, v: int) -> int:
        k = depth[v] - depth[u]
        return (hash1[v] - hash1[u] * pow(BASE, k, MOD) % MOD) % MOD

    def get_hash2(u: int, v: int) -> int:
        k = depth[u]
        return (hash2[v] - hash2[u]) * pow(pow(BASE, k, MOD), MOD - 2, MOD) % MOD

    
    for _ in range(sint()):
        x, y = mint()
        p = get_lca(x, y)
        pp = pa[0][p]
        hx1, hx2 = get_hash1(pp, x), get_hash2(pp, x)
        hy1, hy2 = get_hash1(p, y), get_hash2(p, y)
        h1 = (hx2 * pow(BASE, depth[y] - depth[p], MOD) + hy1) % MOD
        h2 = (hy2 * pow(BASE, depth[x] - depth[p] + 1, MOD) + hx1) % MOD
        
        print("YES" if h1 == h2 else "NO")

solve()

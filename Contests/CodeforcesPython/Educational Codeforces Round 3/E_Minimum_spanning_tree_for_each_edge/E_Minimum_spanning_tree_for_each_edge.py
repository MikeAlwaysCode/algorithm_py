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
    n, m = mint()
    ans = [0] * m
    edges = []
    ev = [set() for _ in range(n)]
    for i in range(m):
        u, v, w = mint()
        u -= 1
        v -= 1
        edges.append((w, u, v))
        ev[u].add(i)
        ev[v].add(i)
        ans[i] += w
    
    edges.sort()

    fa = list(range(n))
    def find(x: int):
        cur = x
        while x != fa[x]:
            x = fa[x]
        while fa[cur] != x:
            fa[cur], cur = x, fa[cur]
        return x
    
    g = 0
    for w, u, v in edges:
        fu, fv = find(u), find(v)
        if fu == fv:
            continue
        g += w
        if len(ev[fu]) > len(ev[fv]):
            fu, fv = fv, fu
        fa[fu] = fa[fv]
        for i in ev[fu] & ev[fv]:
            ans[i] -= w
        ev[fv] |= ev[fu]

    for i in range(m):
        print(ans[i] + g)


solve()

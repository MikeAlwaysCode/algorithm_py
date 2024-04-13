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
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    fb = [1, 1]
    while fb[-1] + fb[-2] <= n:
        fb.append(fb[-1] + fb[-2])
    
    if fb[-1] != n:
        print("NO")
        return
    
    parent = [-1] * n
    sz = [1] * n
    q = [0]
    order = []
    while q:
        u = q.pop()
        order.append(u)
        for v in g[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            q.append(v)
    for u in order[::-1]:
        if parent[u] != -1:
            sz[parent[u]] += sz[u]

    


solve()

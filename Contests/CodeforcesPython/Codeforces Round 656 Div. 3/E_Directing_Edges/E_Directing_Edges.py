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
    edges = []
    g = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    for _ in range(m):
        t, u, v = mint()
        edges.append([t, u, v])
        if t == 1:
            g[u].append(v)
            deg[v] += 1

    q = [i for i in range(1, n + 1) if deg[i] == 0]
    time = [0] * (n + 1)
    step = 0
    while q:
        tmp = q
        q = []
        for u in tmp:
            time[u] = step
            for v in g[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)
        step += 1
    
    if any(deg):
        print("NO")
        return
    
    print("YES")
    for t, u, v in edges:
        if t == 0 and (time[u] > time[v] or (time[u] == time[v] and u > v)):
            u, v = v, u
        print(u, v)


for _ in range(int(input())):
    solve()

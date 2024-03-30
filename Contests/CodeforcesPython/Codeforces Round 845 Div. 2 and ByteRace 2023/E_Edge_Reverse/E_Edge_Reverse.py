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

def find_SCC(graph, x: int):
    SCC, S, P = [], [], []
    depth = [0] * len(graph)
 
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            d = depth[~node] - 1
            if P[-1] > d:
                SCC.append(S[d:])
                del S[d:], P[-1]
                for node in SCC[-1]:
                    depth[node] = -1
        elif depth[node] > 0:
            while P[-1] > depth[node]:
                P.pop()
        elif depth[node] == 0:
            S.append(node)
            P.append(len(S))
            depth[node] = len(S)
            stack.append(~node)
            # stack += graph[node]
            for v, w in graph[node]:
                if w <= x:
                    stack.append(v)
    return SCC[::-1]

def solve() -> None:
    n, m = mint()
    g = [[] for _ in range(n)]
    ws = {0}
    for _ in range(m):
        u, v, w = mint()
        u -= 1
        v -= 1
        g[u].append((v, 0))
        g[v].append((u, w))
        ws.add(w)
    
    def check(x: int) -> bool:
        scc = find_SCC(g, x)
        m = len(scc)
        din = [0] * m
        idx = [-1] * n
        for i, s in enumerate(scc):
            for u in s:
                idx[u] = i
        for u in range(n):
            for v, w in g[u]:
                if idx[v] == idx[u] or w > x:
                    continue
                din[idx[v]] += 1
        return din.count(0) == 1

    ws = sorted(ws)
    l, r = 0, len(ws)
    while l < r:
        mid = (l + r) >> 1
        if check(ws[mid]):
            r = mid
        else:
            l = mid + 1
    print(-1 if r >= len(ws) else ws[r])


for _ in range(int(input())):
    solve()

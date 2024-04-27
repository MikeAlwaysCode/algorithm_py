import sys
from collections import deque

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

def find_SCC(graph):
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
            stack += graph[node]
    return SCC[::-1]

def solve() -> None:
    input()
    n, m = mint()
    g = [[] for _ in range(n)]
    ans = [0] * n
    cycle = [False] * n
    for _ in range(m):
        u, v = mint()
        g[u - 1].append(v - 1)
        if u == v:
            cycle[u - 1] = True
    
    scc = find_SCC(g)
    for scc in find_SCC(g):
        if len(scc) == 1:
            continue
        for u in scc:
            cycle[u] = True
    
    seen = [False] * n
    seen[0] = True
    ans[0] = -1 if cycle[0] else 1
    q = deque([(0, ans[0])])
    while q:
        u, t = q.popleft()
        for v in g[u]:
            if seen[v] and (ans[v] == -1 or (t != -1 and ans[v] == 2)):
                continue
            seen[v] = True
            if t == -1 or cycle[v]:
                ans[v] = -1
            elif 0 <= ans[v] < 2:
                ans[v] += 1
            q.append((v, ans[v]))

    print(*ans)

for _ in range(int(input())):
    solve()

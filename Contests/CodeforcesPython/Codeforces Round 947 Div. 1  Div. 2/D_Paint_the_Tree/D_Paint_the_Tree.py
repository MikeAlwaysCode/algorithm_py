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

def solve() -> None:
    n = sint()
    a, b = mint()
    a -= 1
    b -= 1
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    depth = [0] * n
    parent = [-1] * n
    def bfs(s: int, depth: list, parent: list) -> int:
        depth[s], parent[s] = 0, -1
        q = deque([s])
        mxd = 0
        while q:
            u = q.popleft()
            for v in g[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                mxd = max(mxd, depth[v])
                q.append(v)
        return mxd

    d = bfs(a, depth, parent)
    if a == b:
        print((n - 1) * 2 - d)
        return
    k = (depth[b] + 1) // 2
    for _ in range(k):
        b = parent[b]
    
    d = bfs(b, depth, parent)
    print(k + (n - 1) * 2 - d)


for _ in range(int(input())):
    solve()

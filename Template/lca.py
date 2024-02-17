from collections import *


class LCA:
    def __init__(self, N):
        self.edge = [[] for _ in range(N)]
        self.parent = [0]*N
        self.N = N
        self.K = N.bit_length()
        self.db = [[0]*N for _ in range(self.K)]
        self.depth = [-1]*N
    def add_edges(self, ind=1, bi=False):
        for a,b in [ints() for _ in range(self.N-1)]:
            a -= ind; b -= ind
            self.edge[a].append(b)
            self.parent[b] = a
            if bi: self.edge[b].append(a)
    def add_edge(self, a, b, ind=1, bi=False):
        a -= ind; b -= ind
        self.edge[a].append(b)
        self.parent[b] = a
        if bi: self.edge[b].append(a)
    def bfs(self, start):
        visited = [False]*self.N
        que = deque([start])
        visited[start] = True
        while que:
            v = que.popleft()
            for u in self.edge[v]:
                if not visited[u]:
                    visited[u] = True
                    que.append(u)
        return v
    def doubling(self, root):
        que = deque([root])
        self.depth[root] = 0
        while que:
            v = que.popleft()
            for u in self.edge[v]:
                if self.depth[u]>=0:continue
                self.depth[u] = self.depth[v] + 1
                self.parent[u] = v
                que.append(u)
        self.db[0] = self.parent[:]
        for i in range(1,self.K):
            for j in range(self.N):
                self.db[i][j] = self.db[i-1][self.db[i-1][j]]
    def go_up(self, v, x):
        p = 0
        while x:
            if x % 2:
                v = self.db[p][v]
            p += 1
            x >>= 1
        return v
    def lca(self, u, v):
        d = self.depth[u]-self.depth[v]
        if d >= 0:
            u = self.go_up(u,d)
        else:
            v = self.go_up(v,-d)
        if u == v: return u
        for p in range(self.K-1,-1,-1):
            if self.db[p][u] != self.db[p][v]:
                u, v = self.db[p][u], self.db[p][v]
        return self.db[0][u]


def solve() -> None:
    n = int(input())
    G1 = LCA(n)
    G2 = LCA(n)
    G1.add_edges(bi = True)
    L = G1.bfs(0)
    G1.doubling(L)
    G2.edge = G1.edge[:]
    R = G2.bfs(L)
    G2.doubling(R)
    
    q = int(input())
    for i in range(q):
        u, k = map(int, input().split())
        if G1.depth[u - 1] >= k:
            print(G1.go_up(u - 1, k) + 1)
        elif G2.depth[u - 1] >= k:
            print(G2.go_up(u - 1, k) + 1)
        else:
            print(-1)
# t = int(input())
t = 1
for _ in range(t):
    solve()

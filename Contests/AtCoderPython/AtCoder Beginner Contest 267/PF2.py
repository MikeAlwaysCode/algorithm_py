"""
    LCA 最小共通祖先
"""
import sys; input = sys.stdin.readline
I = lambda:map(int,input().split())
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
        for a,b in [tuple(I()) for _ in range(self.N-1)]:
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
            for j in range(N):
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

N = int(*I())
G = LCA(N);G2 = LCA(N)
G.add_edges(ind=1, bi=True)
L = G.bfs(0)
G.doubling(L)
R = G.bfs(L)
G2.edge = G.edge[:]
G2.doubling(R)
def solve(u,k):
    G3 = G2 if G.depth[u-1] < G2.depth[u-1] else G
    if G3.depth[u-1] < k: return -1
    return G3.go_up(u-1,k)+1
print(*[solve(*I())for _ in range(int(*I()))],sep='\n')
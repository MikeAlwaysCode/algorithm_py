class LCA:
    def __init__(self, g, root, f=max, ide_ele=0):
        # g[v]: (cost, u)
        self.n = len(g)
        self.root = root
        self.f = f
        self.ide_ele = ide_ele
        self.num = (self.n).bit_length()
        self.depth = [0]*self.n
        self.parent = [[-1]*self.n for i in range(self.num)]
        self.size = [1]*n
 
        s = [root]
        order = []
        while s:
            v = s.pop()
            order.append(v)
            for u in g[v]:
                if u == self.parent[0][v]:
                    continue
                self.parent[0][u] = v
                self.depth[u] = self.depth[v]+1
                s.append(u)
        order.reverse()
        for v in order:
            p = self.parent[0][v]
            if p != -1:
                self.size[p] += self.size[v]
 
        # doubling
        for k in range(self.num-1):
            for v in range(self.n):
                if self.parent[k][v] == -1:
                    self.parent[k+1][v] = -1
                else:
                    self.parent[k+1][v] = self.parent[k][self.parent[k][v]]
 
    def getLCA(self, u, v):
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        for k in range(self.num):
            if ((self.depth[v]-self.depth[u]) >> k) & 1:
                v = self.parent[k][v]
        if u == v:
            return u
 
        for k in reversed(range(self.num)):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]
 
    def search(self, v, x):
        for k in reversed(range(self.num)):
            if (x>>k)&1:
                v = self.parent[k][v]
        return v
    
    def dist(self, u, v):
        return self.depth[u] + self.depth[v] - self.depth[self.getLCA(u, v)] * 2
 
# n, m = MII()
# path = [[] for _ in range(n)]
# for _ in range(n - 1):
#     u, v = GMI()
#     path[u].append(v)
#     path[v].append(u)
#  
# lca = LCA(path, 0)
 
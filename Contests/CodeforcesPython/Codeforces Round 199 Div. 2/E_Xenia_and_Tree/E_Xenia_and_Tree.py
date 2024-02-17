import math
import os
import sys
from collections import deque
from io import BytesIO, IOBase

# region fastio
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
        
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
# input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

def GMI():
    return map(lambda x: int(x) - 1, input().split())

# MOD = 998_244_353
# MOD = 10 ** 9 + 7
# DIR4 = ((-1, 0), (0, 1), (1, 0), (0, -1)) #URDL
# DIR8 = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

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
        self.size = [1]*self.n
 
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

def solve() -> None:
    n, m = mint()
    
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = mint()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    '''
    k = n.bit_length()
    parent = [[0] * n for _ in range(k)]
    depth = [-1] * n
    depth[0] = 0

    q = [0]
    while q:
        u = q.pop()
        for v in g[u]:
            if depth[v] >= 0:continue
            depth[v] = depth[u] + 1
            parent[0][v] = u
            q.append(v)
            
    for i in range(1, k):
        for j in range(n):
            if (p := parent[i - 1][j]) != -1:
                parent[i][j] = parent[i-1][p]

    def go_up(u, k):
        for i in range(k.bit_length()):
            if (k >> i) & 1:
                u = parent[i][u]
        return u
    
    def lca(u, v):
        d = depth[u] - depth[v]
        if d >= 0:
            u = go_up(u, d)
        else:
            v = go_up(v, -d)
        if u == v: return u
        for p in range(k-1, -1, -1):
            if parent[p][u] != parent[p][v]:
                u, v = parent[p][u], parent[p][v]
        return parent[0][u]
    
    def dist(u, v):
        return depth[u] + depth[v] - depth[lca(u, v)] * 2
    '''

    lca = LCA(g, 0)
    red_nodes = [0]
    dis = [math.inf] * n

    for _ in range(m):
        t, u = GMI()
        if t:
            if len(red_nodes) >= 100:
                q = deque(red_nodes)
                for x in red_nodes:
                    dis[x] = 0
                while q:
                    x = q.popleft()
                    for y in g[x]:
                        if dis[x] + 1 < dis[y]:
                            dis[y] = dis[x] + 1
                            q.append(y)
                red_nodes = []
        
            ans = dis[u]
            for v in red_nodes:
                ans = min(ans, lca.dist(u, v))
            print(ans)
        else:
            red_nodes.append(u)

solve()

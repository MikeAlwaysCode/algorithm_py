import bisect
import itertools
import math
import os
import random
import sys
from collections import *
from functools import reduce
from heapq import *
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
ints = lambda: list(map(int, input().split()))
# endregion fastio

# region interactive
def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)
# endregion interactive

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

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
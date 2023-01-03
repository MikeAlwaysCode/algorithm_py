import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

# Sample Inputs/Output 
# region fastio
import sys, os
from io import BytesIO, IOBase
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

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n, m = map(int, input().split())
    # tree = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        # tree[u].append(v)
        # tree[v].append(u)
        edges.append((w, u, v))

    query = ints()

    edges.sort()

    fa = list(range(n + 1))
    def find(x):
        # if fa[x] != x:
        #     fa[x] = find(fa[x])
        # return fa[x]
        cur = x
        while x != fa[x]:
            x = fa[x]
        if cur != x:
            fa[cur], cur = x, fa[x]
        return x
    
    size = [1] * (n + 1)
    ans = [0] * m
    cnt = j = 0

    for qw, i in sorted(zip(query, range(m))):
        while j < n - 1 and edges[j][0] <= qw:
            fu = find(edges[j][1])
            fv = find(edges[j][2])
            if fu != fv:
                cnt += size[fu] * size[fv]
                size[fu] += size[fv]
                fa[fv] = fu
            j += 1
        ans[i] = cnt
    print(*ans)

t = 1
for _ in range(t):
    solve()
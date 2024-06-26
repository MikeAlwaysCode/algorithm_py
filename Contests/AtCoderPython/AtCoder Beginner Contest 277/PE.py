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

# MOD = 998244353
# MOD = 10 ** 9 + 7
DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, a = map(int, input().split())
        graph[u].append((v, a))
        graph[v].append((u, a))

    switches = set(ints())
    visited = [[False] * 2 for _ in range(n + 1)]
    
    q = [(1, 0)] # 位置，开关次数
    visited[1][0] = True
    ans = 0
    while q:
        tmp = q
        q = []
        ans += 1
        for x, hit in tmp:
            for v, a in graph[x]:
                if a ^ hit:     # 当前开关可过
                    if v == n:
                        print(ans)
                        return
                    if not visited[v][hit]:
                        visited[v][hit] = True
                        q.append((v, hit))
                if a == hit and x in switches:     # 需要按开关
                    if v == n:
                        print(ans)
                        return
                    if not visited[v][hit^1]:
                        visited[v][hit^1] = True
                        q.append((v, hit^1))

    print(-1)

# t = int(input())
# for _ in range(t):
solve()
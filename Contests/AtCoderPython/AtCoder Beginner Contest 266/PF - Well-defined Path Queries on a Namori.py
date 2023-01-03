import bisect
import collections
import itertools
import math
import os
import random
import sys
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

def solve() -> None:
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    indegrees = [0] * (n + 1)
    for _ in range(n):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        indegrees[u] += 1
        indegrees[v] += 1


    # # DFS找环
    # circle = set()
    # parent = [-1] * (n + 1)
    # dfn = [0] * (n + 1)
    # idx = 0
    # def getCircle(u: int):
    #     nonlocal idx
    #     idx += 1
    #     dfn[u] = idx
    #     for v in graph[u]:
    #         if v == parent[u]: continue
    #         if dfn[v]:
    #             if dfn[v] < dfn[u]: continue
    #             # 之前有另一条路径到达过v，则u到v为环
    #             circle.add(v)
    #             while v != u:
    #                 circle.add(parent[v])
    #                 v = parent[v]
    #         else:
    #             parent[v] = u
    #             getCircle(v)
    # getCircle(1)

    # TopoSort找环
    q = collections.deque(i for i, v in enumerate(indegrees) if v == 1)
                    
    while q:
        cur = q.popleft()
        for x in graph[cur]:
            indegrees[x] -= 1
            if indegrees[x] == 1:
                q.append(x)
    
    # circle = set(i for i, v in enumerate(indegrees) if v > 1)

    # print(circle)
    connect = [0] * (n + 1)

    # for x in circle:
    #     connect[x] = x
    # q = collections.deque(circle)

    q = collections.deque(i for i, v in enumerate(indegrees) if v > 1)
    for x in q:
        connect[x] = x

    while q:
        x = q.popleft()
        for y in graph[x]:
            if connect[y]: continue
            connect[y] = connect[x]
            q.append(y)
    # print(connect)

    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        if connect[u] != connect[v]:
            print("No")
        else:
            print("Yes")

# sys.setrecursionlimit(500000)
# t = int(input())
t = 1
for _ in range(t):
    solve()
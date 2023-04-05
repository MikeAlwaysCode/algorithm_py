import itertools
import math
import os
import random
import sys
from bisect import bisect, bisect_left
from collections import *
from functools import reduce
from heapq import heapify, heappop, heappush
from io import BytesIO, IOBase
from string import *

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
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    q = deque([(0, -1)])
    l = 0
    while q:
        u, p = q.popleft()
        l = u
        for v in g[u]:
            if v == p: continue
            q.append((v, u))
    
    q = deque([(l, -1)])
    dis1 = [0] * n
    r = 0
    while q:
        u, p = q.popleft()
        r = u
        for v in g[u]:
            if v == p: continue
            dis1[v] = dis1[u] + 1
            q.append((v, u))
            
    q = deque([(r, -1)])
    dis2 = [0] * n
    while q:
        u, p = q.popleft()
        for v in g[u]:
            if v == p: continue
            dis2[v] = dis2[u] + 1
            q.append((v, u))
    p = [(max(d1, d2), i) for i, (d1, d2) in enumerate(zip(dis1, dis2))]
    p.sort()
    ans = [0] * n
    j = 0
    for i in range(n):
        k = i + 1
        # j = bisect_left(p, k, key = lambda x: x[0])
        while j < n and p[j][0] < k:
            j += 1
        ans[i] = j + int(j < n)
    print(*ans)


# for _ in range(int(input())):
solve()
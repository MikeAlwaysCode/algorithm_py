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
    n, k = map(int, input().split())
    arr = [-1, 0] + ints()
    # n−1 integers p2,p3,…,pn (1≤pi<i) — the parent of the i-th vertex. Vertex 1 is the root.
    
    h = [0] * (n + 1)
    l, r = 1, n - 1
    while l <= r:
        m = (l + r) // 2
        tot = 0
        
        for i in range(n + 1):
            h[i] = 0

        for i in range(n, 1, -1):
            if h[i] == m - 1 and arr[i] != 1:   # Height = m - 1 and not root, need to cut and the height become m
                tot += 1
            else:   # Height of parent + 1
                h[arr[i]] = max(h[arr[i]], h[i] + 1)

        if tot <= k:
            r = m - 1
        else:
            l = m + 1

    print(l)

t = int(input())
for _ in range(t):
    solve()
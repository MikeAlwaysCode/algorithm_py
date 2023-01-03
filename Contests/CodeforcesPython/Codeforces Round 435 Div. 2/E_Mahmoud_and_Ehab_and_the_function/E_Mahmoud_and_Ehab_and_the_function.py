from bisect import bisect_left
import math
import collections
import random
from heapq import heapify, heappush, heappop
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
    n, m, q = map(int, input().split())
    A = ints()
    B = ints()
    qry = [0] * (q + 1)
    for i in range(1, q+1):
        l, r, x = map(int, input().split())
        qry[i] = qry[i-1]
        if not (r - l) & 1:
            qry[i] += -x if l & 1 else x
    
    sa = sum([-a if i & 1 else a for i, a in enumerate(A)])
    sb = sum([-a if i & 1 else a for i, a in enumerate(B[:n])])
    f = [0] * (m - n + 1)
    f[0] = sa - sb
    for i in range(n, m):
        if i & 1:
            sb -= B[i]
        else:
            sb += B[i]
        if (i-n) & 1:
            sb += B[i-n]
            f[i-n+1] = sa - sb
        else:
            sb -= B[i-n]
            f[i-n+1] = sa + sb
        

    f.sort()
    # print(f)

    for x in qry:
        idx = bisect_left(f, x)
        if idx == m - n + 1:
            print(x - f[idx-1])
        elif f[idx] == x:
            print(0)
        elif idx > 0:
            print(min(f[idx] - x, x - f[idx-1]))
        else:
            print(f[idx] - x)


t = 1
for _ in range(t):
    solve()
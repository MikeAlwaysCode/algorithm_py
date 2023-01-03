import math
import collections
import random
from heapq import heapify, heappush, heappop
from functools import reduce
from bisect import bisect, bisect_left

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
    n = int(input())
    r1, c1, r2, c2, r3, c3 = map(int, input().split())
    x, y = map(int, input().split())

    if r1 == r2:
        kx = r3
    elif r2 == r3:
        kx = r1
    else:
        kx = r2
    
    if c1 == c2:
        ky = c3
    elif c2 == c3:
        ky = c1
    else:
        ky = c2

    if kx == 2 and ky == 2 and max(r1, r2, r3) == 2 and max(c1, c2, c3) == 2 and x != 1 and y != 1:
        print("NO")
        return
    if kx == n-1 and ky == 2 and min(r1, r2, r3) == n-1 and max(c1, c2, c3) == 2 and x != n and y != 1:
        print("NO")
        return
    if kx == 2 and ky == n-1 and max(r1, r2, r3) == 2 and min(c1, c2, c3) == n-1 and x != 1 and y != n:
        print("NO")
        return
    if kx == n-1 and ky == n-1 and min(r1, r2, r3) == n-1 and min(c1, c2, c3) == n-1 and x != n and y != n:
        print("NO")
        return
    
    if not (abs(x - kx)) & 1 and not (abs(y - ky) & 1):
        print("NO")
    else:
        print("YES")

t = int(input())
for _ in range(t):
    solve()
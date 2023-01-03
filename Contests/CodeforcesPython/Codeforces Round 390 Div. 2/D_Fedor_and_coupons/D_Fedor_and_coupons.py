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
    n, k = map(int, input().split())
    arr = []
    for i in range(n):
        l, r = map(int, input().split())
        arr.append((l, r, i + 1))
    
    arr.sort()
    h = []
    mxl = 0
    mx = 0
    ansl = ansr = 0
    for l, r, i in arr:
        if len(h) < k:
            mxl = l
            heappush(h, r)
            if len(h) == k:
                mx = max(0, h[0] - mxl + 1)
                ansl = mxl
                ansr = h[0]
        elif r > h[0]:
            heappop(h)
            heappush(h, r)
            mxl = l

            if h[0] - mxl + 1 > mx:
                mx = h[0] - mxl + 1
                ansl = mxl
                ansr = h[0]
            '''
            first = heappop(h)
            second = heappop(h)

            mnr = min(r, second[1])
            if l - mxl <= mnr - first[1]:
                mxl = l
                heappush(h, second)
                heappush(h, (r, l, i))
            else:
                heappush(h, second)
                heappush(h, first)
            '''

    print(mx)
    ans = []
    for l, r, i in arr:
        if l <= ansl and r >= ansr:
            ans.append(i)
            if len(ans) == k:
                break
    print(*ans)

t = 1
for _ in range(t):
    solve()
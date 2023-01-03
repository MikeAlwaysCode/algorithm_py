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
    p1, t1 = map(int, input().split())
    p2, t2 = map(int, input().split())
    h, s = map(int, input().split())

    k1 = p1 - s
    k2 = p2 - s
    k3 = p1 + p2 - s

    mxt = max(t1, t2)
    ans3 = (h + k3 - 1 ) // k3 * mxt
    ans1 = (h + k1 - 1 ) // k1 * t1
    ans2 = (h + k2 - 1 ) // k2 * t2
    
    # l = min(ans1, ans2, ans3)
    l = min(t1, t2)
    r = max(ans1, ans2, ans3)
    while l < r:
        mid = (l + r) // 2

        # dam1 = k1 * (mid // t1) + k2 * (mid // t2)

        dam = 0
        r3 = mid // mxt
        for i in range(0, r3 + 1):
            tmp = k3 * i + k1 * ((mid - mxt * i) // t1) + k2 * ((mid - mxt * i) // t2)
            dam = max(tmp, dam)

        if dam >= h:
            r = mid
        else:
            l = mid + 1
    print(r)

# t = int(input())
# for _ in range(t):
solve()
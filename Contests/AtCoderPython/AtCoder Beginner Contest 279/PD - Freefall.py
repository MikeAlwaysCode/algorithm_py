import collections
import math
import os
import random
import sys
from functools import reduce
from heapq import heappop, heappush
from io import BytesIO, IOBase

# Sample Inputs/Output 
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
    a, b = map(int, input().split())

    def cal(x: int) -> float:
        # return b * x + a / math.sqrt(1 + x)
        return b * x + math.sqrt(a * a / (1 + x))
    
    l, r = 0, a * a
    ans = cal(0)
    while l < r:
        mid = l + r >> 1
        p = l + mid >> 1
        q = mid + r + 1 >> 1
        curr = cal(p)
        next = cal(q)
        # print(curr, next)
        # while next == curr:
        #     tm += step
        #     step += 1
        #     next = cal(tm)

        if next >= curr:
            if curr < ans:
                # print(mid)
                ans = curr
            r = q - 1
        else:
            if next < ans:
                # print(tm)
                ans = next
            l = p + 1
    # print(l, r)
    print(ans)

# t = int(input())
# for _ in range(t):
solve()
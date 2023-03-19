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
    L, n1, n2 = map(int, input().split())
    A = []
    B = []
    for _ in range(n1):
        v, l = map(int, input().split())
        A.append((v, l))
    for _ in range(n2):
        v, l = map(int, input().split())
        B.append((v, l))

    ans = 0
    i = j = 1
    l1, r1, v1 = 1, A[0][1], A[0][0]
    l2, r2, v2 = 1, B[0][1], B[0][0]
    
    while i < n1 or j < n2:
        if v1 == v2:
            r = min(r1, r2)
            l = max(l1, l2)
            ans += max(0, r - l + 1)

        if r1 > r2:
            l2, r2, v2 = r2 + 1, r2 + B[j][1], B[j][0]
            j += 1
        elif r2 > r1:
            l1, r1, v1 = r1 + 1, r1 + A[i][1], A[i][0]
            i += 1
        else:
            l1, r1, v1 = r1 + 1, r1 + A[i][1], A[i][0]
            i += 1
            l2, r2, v2 = r2 + 1, r2 + B[j][1], B[j][0]
            j += 1
    if v1 == v2:
        r = min(r1, r2)
        l = max(l1, l2)
        ans += max(0, r - l + 1)

    print(ans)

solve()
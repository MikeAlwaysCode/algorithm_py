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
    n, m, k = map(int, input().split())
    A = []
    B = []
    for _ in range(n):
        u, v = map(int, input().split())
        A.append((u, v))
    for _ in range(m):
        u, v = map(int, input().split())
        B.append((u, v))
        
    A.sort(key = lambda x: x[0] / x[1])
    B.sort(key = lambda x: x[0] / x[1])

    k = n * m - k + 1

    def f(a, b):
        return (a[0] + b[0]) / (a[0] + a[1] + b[0] + b[1])
    
    def check(x):
        cnt = 0
        j = m - 1
        for i in range(n):
            while j >= 0 and f(A[i], B[j]) + 0.0000000001 >= x:
                j -= 1
            cnt += j + 1
        return cnt >= k


    l, r = 0, 1
    for _ in range(100):
        mid = (l + r) / 2
        if check(mid):
            r = mid
        else:
            l = mid

    print(r * 100)

solve()
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
    l, r = map(int, input().split())
    if l == r:
        print(l)
        return

    rs = str(r)
    ls = str(l)
    n = len(rs)
    m = len(ls)

    for d in digits[1:]:
        if int(d) < int(ls[0]):
            x = int(d * (m + 1))
        elif int(d) >= int(ls[0]):
            x = int(d * m)
            
        if l <= x <= r:
            print(x)
            return
    
    s = []
    i = 0
    mn, mx = 10, -1
    while i < m and rs[i] == ls[i]:
        mn = min(mn, int(rs[i]))
        mx = max(mx, int(rs[i]))
        s.append(rs[i])
        i += 1
    
    if i == m - 1:
        p = int(s[-1])
        if int(rs[i]) < p:
            print(r)
            return
        else:
            print(l)
            return

    diff = 10
    ans = l
    left = m - i - 1

    for k in range(int(ls[i]), int(rs[i]) + 1):
        for d in digits:
            cmn = min(mn, int(d), k)
            cmx = max(mx, int(d), k)

            x = int("".join(s) + str(k) + d * left)
            
            if l <= x <= r and cmx - cmn < diff:
                diff = cmx - cmn
                ans = x

    print(ans)
    

for _ in range(int(input())):
    solve()
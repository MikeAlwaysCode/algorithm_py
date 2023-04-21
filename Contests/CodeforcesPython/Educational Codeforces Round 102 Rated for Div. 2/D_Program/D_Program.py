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
    n, m = map(int, input().split())
    s = input()
    
    pre = [0] * (n + 1)
    pre_mx = [0] * (n + 1)
    pre_mn = [0] * (n + 1)
    for i, c in enumerate(s):
        if c == "+":
            pre[i + 1] = pre[i] + 1
        else:
            pre[i + 1] = pre[i] - 1
        pre_mx[i + 1] = max(pre_mx[i], pre[i + 1])
        pre_mn[i + 1] = min(pre_mn[i], pre[i + 1])
    
    suf_mx = [0] * (n + 1)
    suf_mn = [0] * (n + 1)
    mx = mn = pre[-1]
    for i in range(n - 1, -1, -1):
        mx = max(mx, pre[i])
        mn = min(mn, pre[i])
        suf_mx[i] = max(suf_mx[i], mx - pre[i])
        suf_mn[i] = min(suf_mn[i], mn - pre[i])
    
    for _ in range(m):
        l, r = map(int, input().split())
        cmx = max(pre_mx[l - 1], pre[l - 1] + suf_mx[r])
        cmn = min(pre_mn[l - 1], pre[l - 1] + suf_mn[r])
        # print(cmx, cmn)
        print(cmx - cmn + 1)

for _ in range(int(input())):
    solve()
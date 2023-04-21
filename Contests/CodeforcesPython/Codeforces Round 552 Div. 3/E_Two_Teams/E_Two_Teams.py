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
    n, k = map(int, input().split())
    arr = ints()
    
    ans = [0] * n
    # idx = sorted(range(n), key = lambda x: -arr[x])
    # prev = list(range(-1, n - 1))
    # next = list(range(1, n + 1))
    idx = [0] * n
    prev = [0] * n
    next = [0] * n
    for i, a in enumerate(arr):
        idx[a - 1] = i
        prev[i] = i - 1
        next[i] = i + 1
    step = 1
    # for x in idx:
    for x in range(n - 1, -1, -1):
        x = idx[x]
        if ans[x]: continue
        ans[x] = step
        
        i = j = x
        for _ in range(k):
            if i > 0:
                i = prev[i]
                if i >= 0:
                    ans[i] = step
            if j < n - 1:
                j = next[j]
                if j < n:
                    ans[j] = step
                    
        if i >= 0 and prev[i] >= 0:
            if j < n:
                next[prev[i]] = next[j]
            else:
                next[prev[i]] = j
        if j < n and next[j] < n:
            if i >= 0:
                prev[next[j]] = prev[i]
            else:
                prev[next[j]] = i

        step ^= 3

    print(*ans, sep="")

# for _ in range(int(input())):
solve()
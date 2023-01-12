import collections
import math
import os
import random
import sys
from bisect import bisect, bisect_left
from functools import reduce
from heapq import heapify, heappop, heappush
from io import BytesIO, IOBase

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
    s = input()
    n = len(s)

    cnt = collections.Counter(s)
    if len(cnt) == 1:
        print(s[0], s[1:-1], s[-1])
        return

    i = 1
    while i < n and s[i] == s[0]:
        i += 1

    if i == n - 1:
        if s[i] > s[0]:
            print(s[:i - 1], s[i - 1], s[i])
        else:
            print(s[0], s[1:i], s[i])
        return
    
    j = i + 1
    if s[i] < s[0]:
        while j < n and s[j] < s[j - 1]:
            j += 1
        if j < n:
            print(s[:j - 1], s[j - 1], s[j:])
            return
    else:
        while j < n and s[j] >= s[j - 1]:
            j += 1
        if j < n:
            print(s[:j - 1], s[j - 1], s[j:])
            return
        if s[-1] == s[-2]:
            print(s[:-2], s[-2], s[-1])
            return

    print(":(")

t = int(input())
for _ in range(t):
    solve()
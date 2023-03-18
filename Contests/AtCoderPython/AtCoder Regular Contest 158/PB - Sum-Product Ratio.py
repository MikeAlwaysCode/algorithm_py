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
    n = int(input())
    arr = ints()

    neg = [a for a in arr if a < 0]
    pos = [a for a in arr if a > 0]

    neg.sort()
    pos.sort()

    def f(a, b, c):
        return (a + b + c) / (a * b * c)
    
    if not neg:
        mn = f(pos[-1], pos[-2], pos[-3])
        mx = f(pos[0], pos[1], pos[2])
    else:
        mn = math.inf
        mx = - math.inf

        if len(neg) > 2:
            mn = f(neg[0], neg[1], neg[2])
            mx = f(neg[-1], neg[-2], neg[-3])

        if len(pos) >= 2:
            mn = min(mn, f(neg[-1], pos[0], pos[1]))
            i = 0
            while i < len(pos) - 2 and (neg[-1] + pos[i] + pos[i + 1]) <= 0:
                i += 1
            mn = min(mn, f(neg[-1], pos[i], pos[i + 1]))
            
            mx = max(mx, f(neg[-1], pos[0], pos[1]))
            if neg[-1] + pos[0] + pos[1] > 0:
                mx = max(mx, f(neg[-1], pos[-1], pos[-2]))
            i = len(neg) - 1
            while i > 0 and neg[i] + pos[0] + pos[1] >= 0:
                i -= 1
            mx = max(mx, f(neg[i], pos[-1], pos[-2]))

        if pos and len(neg) >= 2:
            mn = min(mn, f(neg[-1], neg[-2], pos[0]))
            i = len(neg) - 2
            while i > 0 and (neg[i] + neg[i + 1] + pos[0]) >= 0:
                i -= 1
            mn = min(mn, f(neg[i], neg[i+1], pos[0]))
            
            mx = max(mx, f(neg[-1], neg[-2], pos[0]))
            if neg[-1] + neg[-2] + pos[0] < 0:
                mx = max(mx, f(neg[0], neg[1], pos[0]))
            i = 0
            while i < len(pos) - 2 and neg[-1] + neg[-2] + pos[i] <= 0:
                i += 1
            mx = max(mx, f(neg[0], neg[1], pos[i]))

        if len(pos) > 2:
            mn = min(mn, f(pos[-1], pos[-2], pos[-3]))
            mx = max(mx, f(pos[0], pos[1], pos[2]))

    print(mn)
    print(mx)

solve()
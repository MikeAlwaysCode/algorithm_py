import bisect
import collections
import itertools
import math
import os
import random
import sys
from functools import reduce, lru_cache
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

MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    s, l, r = input().split()
    
    if len(l) < len(r):
        l = "0" * (len(r) - len(l)) + l
        
    @lru_cache(None)
    def f(i: int, j: int, upLimit: bool, downLimit: bool, isNum: bool):
        if i == len(s):
            if j == len(r):
                return 1
            
            if s == "0" and isNum:
                return 0
            
            mx = int(r[j:]) if upLimit else pow(10, len(r) - j)
            mn = int(l[j:]) if downLimit else 0
            return mx - mn

        if len(s) - i > len(r) - j:
            return 0
        
        res = 0
        up = int(r[j]) if upLimit else 9
        down = int(l[j]) if downLimit else 1 - int(isNum)

        for d in range(down, up + 1):
            if i == 0:
                res += f(i, j + 1, upLimit and d == up, downLimit and d == down)
            if d == int(s[i]):
                res += f(i + 1, j + 1, upLimit and d == up, downLimit and d == down)
        return res
    print(f(0, 0, True, True))


for _ in range(int(input())):
    solve()
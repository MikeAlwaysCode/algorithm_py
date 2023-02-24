import collections
import itertools
import math
import os
import random
import sys
from bisect import bisect, bisect_left
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

# d = collections.Counter()
# def init():
#     n, mx = 1, 2 * 10 ** 9
#     while n * (n - 1) <= mx:
#         d[n * (n - 1) // 2] = n
#         n += 1

def cal(c) -> int:
    x = (math.isqrt(c * 8 + 1) + 1) // 2
    if x * (x - 1) // 2 == c:
        return x
    return -1

def solve() -> None:
    a00, a01, a10, a11 = map(int, input().split())

    # n, m = d[a00], d[a11]
    n, m = cal(a00), cal(a11)
    
    # if not n or not m:
    if n < 0 or m < 0:
        print("Impossible")
        return

    if a01 == 0 and a10 == 0:
        if a00 == 0 and a11 == 0:
            print("0")
            return
        if a00 and a11:
            print("Impossible")
            return
        elif a00:
            print("0" * n)
            return
        elif a11:
            print("1" * m)
            return

    if a01 + a10 != n * m:
        if a00 == 0 and a01 + a10 == m:
            n = 1
        elif a11 == 0 and a10 + a10 == n:
            m = 1
        else:
            print("Impossible")
            return
    
    r1 = a01 // n
    l0 = a01 % n
    r0 = n - l0
    m1 = 1 if l0 else 0
    if l0: a10 -= n - l0
    l1 = m - m1 - r1
    ans = "1" * l1 + "0" * l0 + "1" * m1 + "0" * r0 + "1" * r1
    print(ans)

# init()
# for _ in range(int(input())):
solve()
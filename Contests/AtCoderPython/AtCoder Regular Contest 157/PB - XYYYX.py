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
    n, k = map(int, input().split())
    s = input()

    # def check(m) -> bool:
    #     cntx = l = 0
    #     for r in range(n):
    #         if s[r] == 'X':
    #             cntx += 1
    #         if r - l > m:
    #             if s[l] == 'X':
    #                 cntx -= 1
    #             l += 1

    #         # if r - l == m and (cntx == k or (k > cntx and n - r + l - 1 >= k - cntx)):
    #         if r - l == m and k >= cntx and n - r + l - 1 >= k - cntx:
    #             return True
    #     return False

    # l, r = 0, n - 1

    # while l < r:
    #     mid = l + r + 1 >> 1
    #     if check(mid):
    #         l = mid
    #     else:
    #         r = mid - 1

    # print(l)

    ans = 0
    totx = s.count('X')
    if totx == k:
        print(n - 1)
        return
    elif totx < k:
        pres = [0] * (n + 1)
        for i in range(1, n):
            pres[i + 1] = pres[i]
            if s[i - 1] == 'X' and s[i] == 'X':
                pres[i + 1] += 1

        cntx = k - totx
        for i in range(n):
            if s[i] == 'Y':
                cntx -= 1
                if cntx == 0:
                    ans = n - i - 2 + pres[i + 1]
                    break
        
        cntx = k - totx
        for i in range(n - 1, -1, -1):
            if s[i] == 'Y':
                cntx -= 1
                if cntx == 0:
                    ans = max(ans, i - 1 + pres[-1] - pres[i])
                    break
    else:
        pres = [0] * (n + 1)
        for i in range(1, n):
            pres[i + 1] = pres[i]
            if s[i - 1] == 'Y' and s[i] == 'Y':
                pres[i + 1] += 1

        cntx = l = 0
        for r in range(n):
            if s[r] == 'X':
                cntx += 1
            while cntx > k:
                if s[l] == 'X':
                    cntx -= 1
                l += 1
            if cntx == k:
                ans = max(ans, r - l + pres[l] + pres[-1] - pres[r + 1])
            # elif n - r + l - 1 >= k - cntx:
            #     ans = max(ans, r - l)

    print(ans)

solve()
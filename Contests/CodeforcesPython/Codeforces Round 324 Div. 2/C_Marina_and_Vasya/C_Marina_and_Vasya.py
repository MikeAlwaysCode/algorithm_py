import collections
import itertools
import math
import os
import random
from string import ascii_lowercase
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
    n, t = map(int, input().split())
    s1 = input()
    s2 = input()
    
    diff = sum(c1 != c2 for c1, c2 in zip(s1, s2))
    if t < (diff + 1) // 2:
        print(-1)
        return
    
    each = max(0, diff - t)
    more = max(0, t - diff)
    ans = [''] * n
    e1 = e2 = 0
    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 == c2:
            if more:
                ans[i] = chr((ord(c1) - 96) % 26 + 97)  # Next different letter
                more -= 1
            else:
                ans[i] = c1
        else:
            if e1 < each:
                ans[i] = c2
                e1 += 1
            elif e2 < each:
                ans[i] = c1
                e2 += 1
            else:
                for c in ascii_lowercase:
                    if c != c1 and c != c2:
                        ans[i] = c
                        break
    print("".join(ans))

# t = int(input())
# for _ in range(t):
solve()
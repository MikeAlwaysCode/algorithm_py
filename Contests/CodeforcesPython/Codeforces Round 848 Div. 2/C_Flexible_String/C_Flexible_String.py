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
    sa = input()
    sb = input()
    ans = pre = 0
    for i in range(n):
        if sa[i] == sb[i]:
            pre += 1
            ans += pre
        else:
            pre = 0
            
    if k == 0:
        print(ans)
        return

    s = list(set(sa))
    d = {c:i for i, c in enumerate(s)}
    m = len(s)
    k = min(m, k)
    # for comb in itertools.combinations(range(m), k):
    #     mask = 0
    #     for j in comb:
    #         mask |= 1 << j
    # for mask in range(1 << m):
    #     # if mask.bit_count() != k: continue
    #     if bin(mask).count("1") != k: continue
    mask = (1 << k) - 1
    while mask < 1 << m:
        curr = pre = 0
        for i in range(n):
            if sa[i] == sb[i] or (mask >> d[sa[i]]) & 1:
                pre += 1
                curr += pre
            else:
                pre = 0
        ans = max(ans, curr)

        lb = mask & -mask
        x = mask + lb
        mask = (x ^ mask) // lb >> 2 | x

    print(ans)

t = int(input())
for _ in range(t):
    solve()
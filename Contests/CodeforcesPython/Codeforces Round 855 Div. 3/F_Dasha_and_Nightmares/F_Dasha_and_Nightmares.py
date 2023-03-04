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

MX = (1 << 26) - 1

def solve() -> None:
    n = int(input())
    ans = 0
    
    f = collections.Counter()
    ext = [0] * n
    mask = [0] * n
    for j in range(n):
        s = input()
        cnt = collections.Counter(s)
        maske = masks = 0
        for i, c in enumerate(ascii_lowercase):
            if cnt[c]:
                maske |= 1 << i
            if cnt[c] & 1:
                masks |= 1 << i
        ext[j] = maske
        mask[j] = masks
        
    for i, c in enumerate(ascii_lowercase):
        for j in range(n):
            if ext[j] >> i & 1: continue
            ans += f[MX ^ mask[j] ^ (1 << i)]
            f[mask[j]] += 1
        
        f.clear()
        # for j in range(n):
        #     if ext[j] >> i & 1: continue
        #     f[mask[j]] -= 1

    '''
    cnt = [collections.Counter() for _ in range(26)]
    for _ in range(n):
        s = input()
        cc = collections.Counter(s)
        masks = 0
        for i, c in enumerate(ascii_lowercase):
            if cc[c] & 1:
                masks |= 1 << i
        
        maskt = MX ^ masks
        for i, c in enumerate(ascii_lowercase):
            if cc[c]: continue
            ans += cnt[i][maskt ^ (1 << i)]
            cnt[i][masks] += 1
    '''

    print(ans)

# for _ in range(int(input())):
solve()
import collections
import math
import os
import random
import sys
from bisect import bisect, bisect_left
from functools import reduce
from heapq import heapify, heappop, heappush
from io import BytesIO, IOBase

# Sample Inputs/Output 
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

# MOD = 998244353
# MOD = 10 ** 9 + 7
DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n, h = map(int, input().split())
    arr = ints()
    
    arr.sort()
    serum = [2, 2, 3]
    ans = 0
    # dp = [[0] * 8 for _ in range(n + 1)]
    dp = [[0] * 8 for _ in range(2)]
    for i in range(8):
        mul = 1
        for j in range(3):
            if (i >> j) & 1:
                mul *= serum[j]
        dp[0][i] = h * mul
    # print(dp)
    idx = 0
    for a in arr:
        chk = False
        for mask in range(8):
            for i in range(8):
                if (mask | i) != i:
                    # dp[idx^1][i] = 0
                    continue
                mul = 1
                for j in range(3):
                    if (i >> j) & 1 and not (mask >> j) & 1:
                        mul *= serum[j]
                if dp[idx][mask] > a:
                    dp[idx^1][i] = max(dp[idx^1][i], (dp[idx][mask] + a//2) * mul)
                    chk = True
                elif dp[idx][mask] * mul > a:
                    dp[idx^1][i] = max(dp[idx^1][i], dp[idx][mask] * mul + a // 2)
                    chk = True
        if not chk:
            break
        ans += 1
        idx ^= 1
        
    print(ans)

t = int(input())
for _ in range(t):
    solve()
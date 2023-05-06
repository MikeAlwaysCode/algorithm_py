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
MOD = 10 ** 8

def solve() -> None:
    n1, n2, k1, k2 = map(int, input().split())
    dp = [[[[0] * 2 for _ in range(11)] for _ in range(n1 + 1)] for _ in range(n1 + n2 + 1)]    # total,cnta,consecutive,a or b
    dp[0][0][0][0] = 1
    for i in range(1, n1 + n2 + 1):
        for j in range(1, n1 + 1):
            for k in range(1, k1 + 1):
                dp[i][j][k][0] = (dp[i][j][k][0] + dp[i - 1][j - 1][k - 1][0]) % MOD
            for k in range(k2 + 1):
                dp[i][j][1][0] = (dp[i][j][1][0] + dp[i - 1][j - 1][k][1]) % MOD
        
        for j in range(n1 + 1):
            for k in range(1, k2 + 1):
                dp[i][j][k][1] = (dp[i][j][k][1] + dp[i - 1][j][k - 1][1]) % MOD
            for k in range(k1 + 1):
                dp[i][j][1][1] = (dp[i][j][1][1] + dp[i - 1][j][k][0]) % MOD

    ans = 0
    for k in range(1, k1 + 1):
        ans = (ans + dp[n1 + n2][n1][k][0]) % MOD

    for k in range(1, k2 + 1):
        ans = (ans + dp[n1 + n2][n1][k][1]) % MOD

    print(ans)

# for _ in range(int(input())):
solve()
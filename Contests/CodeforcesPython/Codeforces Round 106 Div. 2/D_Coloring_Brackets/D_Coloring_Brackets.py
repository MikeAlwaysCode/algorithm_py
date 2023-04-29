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
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))


def solve() -> None:
    s = input()
    n = len(s)
    dp = [[[0] * 9 for _ in range(n)] for _ in range(n)]
    stk = []
    left = [-1] * n
    for i, c in enumerate(s):
        if c == "(":
            stk.append(i)
        else:
            j = stk.pop()
            for k in range(9):
                c1, c2 = divmod(k, 3)
                if c1 == c2 or (c1 and c2): continue

                # (0, 1), (0, 2), (1, 0), (2, 0)
                if i - j == 1:
                    dp[j][i][k] = 1
                else:
                    for m in range(9):
                        c3, c4 = divmod(m, 3)
                        if (c1 and c1 == c3) or (c2 and c2 == c4): continue
                        dp[j][i][k] += dp[j + 1][i - 1][m]
                        dp[j][i][k] %= MOD
            while j > 0 and left[j - 1] != -1: # 左边有其他括号对
                l, r = left[j - 1], j - 1
                for k in range(9):
                    c1, c2 = divmod(k, 3)
                    for m in range(9):
                        c3, c4 = divmod(m, 3)
                        if c2 and c2 == c3: continue
                        dp[l][i][c1 * 3 + c4] += dp[l][r][k] * dp[j][i][m]
                        dp[l][i][c1 * 3 + c4] %= MOD
                left[i] = j = l
            left[i] = j

    print(sum(dp[0][-1]) % MOD)

# for _ in range(int(input())):
solve()
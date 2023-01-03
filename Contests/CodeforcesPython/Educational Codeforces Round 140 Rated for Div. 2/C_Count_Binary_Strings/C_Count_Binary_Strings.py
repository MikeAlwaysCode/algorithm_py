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
# endregion fastio

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = int(input())
    constraints = [[0] * n for _ in range(n)]
    for i in range(n):
        arr = ints()
        for j in range(i, n):
            constraints[i][j] = arr[j - i]

    def check(cnt, last) -> bool:
        for i in range(cnt):
            # 0 无限制
            if constraints[i][cnt - 1] == 0: continue
            # 1 i ~ cnt 应该全部一样
            if constraints[i][cnt - 1] == 1 and last > i: return False
            # 0 i ~ cnt 应该存在不一样
            if constraints[i][cnt - 1] == 2 and last <= i: return False
        return True

    dp = [[0] * n for _ in range(n + 1)]
    if constraints[0][0] != 2:
        dp[1][0] = 2

    for i in range(1, n):
        for j in range(i):
            # i + 1 = i, i + 1前最后一个不同的元素位置是j合法：dp[i][j] -> dp[i+1][j]
            if check(i + 1, j):
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
            # i + 1 != i, i + 1前最后一个不同的元素位置是i合法：dp[i][j] -> dp[i+1][i]
            if check(i + 1, i):
                dp[i + 1][i] = (dp[i + 1][i] + dp[i][j]) % MOD
        
    ans = 0
    for i in range(n):
        ans = (ans + dp[n][i]) % MOD
        
    print(ans)

# t = int(input())
t = 1
for _ in range(t):
    solve()
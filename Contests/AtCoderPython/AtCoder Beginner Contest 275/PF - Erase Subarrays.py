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
    n, m = map(int, input().split())
    arr = ints()

    dp = [-1] * (m + 1)     # dp[j]: 前面和为j的最小操作数
    pos = [-1] * (m + 1)    # pos[j]：前面和为j最小操作数是dp[j]时的最后取的数的位置
    dp[0] = 1

    for i, a in enumerate(arr):
        for j in range(m - a, -1, -1):
            # 前面不存在和为j的操作
            if dp[j] == -1: continue
            
            if pos[j] == i - 1:
                # i-1能得到和为j的最小操作，加上a操作数不变
                cur = dp[j]
            else:
                # 得到和为j的最小操作数的最后的数在i-1之前，得到j+a时操作数+1
                cur = dp[j] + 1
            # 如果当前是最后一个数，转移的操作数-1
            if i == n - 1:
                cur -= 1
            if dp[j + a] == -1 or cur <= dp[j + a]:
                # 更新最小操作数和最后的数的位置，得到相同的最小操作数的情况下，最后取的数的位置越往后一定越优
                dp[j + a] = cur
                pos[j + a] = i
                
    for ans in dp[1:]:
        print(ans)

# t = int(input())
t = 1
for _ in range(t):
    solve()
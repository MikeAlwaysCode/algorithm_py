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

def solve() -> None:
    s = input()
    n = len(s)

    suff = [0] * n
    cnt = 0
    for i in range(n - 1, -1, -1):
        suff[i] = cnt
        if s[i] == '0':
            cnt += 1
            
    ans = cnt * (10 ** 12 + 1)
    cnt = 0

    for i in range(n):
        ans = min(ans, (cnt + suff[i]) * (10 ** 12 + 1))
            
        if i and s[i] == '0' and s[i - 1] == '1':
            ans = min(ans, (cnt + suff[i] - 1) * (10 ** 12 + 1) + 10 ** 12)

        if ans == 0:
            break
            
        if s[i] == '1':
            cnt += 1
    
    print(ans)
    '''
    dp = [[0] * 2 for _ in range(n)]
    if s[0] == '0':
        dp[0][1] = 10 ** 12 + 1
    else:
        dp[0][0] = 10 ** 12 + 1

    for i in range(1, n):
        if s[i] == '0':
            dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 10 ** 12 + 1
            if s[i - 1] == '1':
                if i > 1:
                    dp[i][1] = min(dp[i][1], dp[i-2][0] + 10 ** 12)
                else:
                    dp[i][1] = 10 ** 12
            dp[i][0] = dp[i-1][0]
        else:
            dp[i][1] = min(dp[i-1][0], dp[i-1][1])
            dp[i][0] = dp[i-1][0] + 10 ** 12 + 1
    
    print(min(dp[-1]))
    '''

for _ in range(int(input())):
    solve()
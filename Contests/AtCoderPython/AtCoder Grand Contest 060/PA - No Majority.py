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

MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = int(input())
    s = input()

    dp = [[0] * 26 for _ in range(n)]

    if s[0] == '?':
        for i in range(26):
            dp[0][i] = 1
    else:
        dp[0][ord(s[0]) - 97] = 1

    if s[1] == '?':
        for i in range(26):
            cnt = 0
            for j in range(26):
                if j == i: continue
                cnt += dp[0][j]
            dp[1][i] = cnt
    else:
        cnt = 0
        i = ord(s[1]) - 97
        for j in range(26):
            if j == i: continue
            cnt += dp[0][j]
        dp[1][i] = cnt

    for i in range(2, n):
        if s[i] == '?':
            for j in range(26):
                cnt = 0
                for k in range(26):
                    if k == j or not dp[i-1][k]: continue
                    for l in range(26):
                        if l == j or l == k: continue
                        # cnt += dp[i-1][k] * dp[i-2][l] % MOD
                        cnt += dp[i-2][l]
                        cnt %= MOD
                dp[i][j] = cnt
        else:
            cnt = 0
            j = ord(s[i]) - 97
            for k in range(26):
                if k == j or not dp[i-1][k]: continue
                for l in range(26):
                    if l == j or l == k: continue
                    # cnt += dp[i-1][k] * dp[i-2][l] % MOD
                    cnt += dp[i-2][l]
                    cnt %= MOD
            dp[i][j] = cnt
    print(dp)
    ans = sum(dp[n - 1]) % MOD

    print(ans)

# t = int(input())
t = 1
for _ in range(t):
    solve()
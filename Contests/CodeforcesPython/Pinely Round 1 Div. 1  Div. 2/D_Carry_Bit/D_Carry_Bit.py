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
MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

mx = 10 ** 6
fact = [1] * (mx + 1)
inverse = [0] * (mx + 1)
def combInit() -> None:
    # 阶乘
    for i in range(1, mx + 1):
        fact[i] = fact[i-1] * i % MOD

    # 逆元
    inverse[mx] = pow(fact[mx], MOD - 2, MOD)
    for i in range(mx, 0, -1):
        inverse[i-1] = inverse[i] * i % MOD

# 组合数
def comb(n: int, m: int, MOD: int) -> int:
    if m < 0 or m > n:
        return 0
    return fact[n] * inverse[m] % MOD * inverse[n-m] % MOD

def solve() -> None:
    n, k = map(int, input().split())

    if k == 0:
        print(pow(3, n, MOD))
        return

    pow3 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow3[i] = pow3[i-1] * 3 % MOD

    ans = 0
    for q in range(1, k + 1):
        # case 1: K+on used, N-(K+on) remaining over on+1
        if q * 2 <= n:
            ans += pow3[n - q * 2] * comb(k - 1, q - 1, MOD) * comb(n - k, q, MOD) % MOD
		# case 2: K+on-1 used, N-(K+on-1) remaining over on
        if q * 2 <= n + 1:
            ans += pow3[n - q * 2] * comb(k - 1, q - 1, MOD) * comb(n - k, q - 1, MOD) % MOD
        ans %= MOD
    
    print(ans)

combInit()
# t = int(input())
# for _ in range(t):
solve()
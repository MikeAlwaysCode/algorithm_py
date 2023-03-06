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

MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

MXN = 10 ** 6
isprime = [True] * (MXN + 1)
MC = 4048
fact = [1] * (MC + 1)
inverse = [0] * (MC + 1)

def init():
    isprime[1] = False
    for i in range(2, MXN + 1):
        if not isprime[i]:
            continue
        for j in range(i + i, MXN + 1, i):
            isprime[j] = False
    
    # 阶乘
    for i in range(1, MC + 1):
        fact[i] = fact[i-1] * i % MOD
    # 逆元
    inverse[MC] = pow(fact[MC], MOD - 2, MOD)
    for i in range(MC, 0, -1):
        inverse[i-1] = inverse[i] * i % MOD

def solve() -> None:
    n = int(input())
    arr = ints()

    cnt = Counter(arr)
    ans = 1
    primes = []
    for k, v in cnt.items():
        if not isprime[k]:
            ans = ans * inverse[v] % MOD
        else:
            primes.append(k)
    
    if len(primes) < n:
        print(0)
        return
    
    dp = [0] * (n + 1)
    dp[0] = 1
    for p in primes:
        c = cnt[p]
        for j in range(n-1, -1, -1):
            # dp[j] = (dp[j] * inverse[c] + dp[j-1] * inverse[c-1]) % MOD
            dp[j+1] = (dp[j+1] + dp[j] * inverse[c-1]) % MOD
            dp[j] = dp[j] * inverse[c] % MOD
    
    ans = ans * dp[n] * fact[n] % MOD
    print(ans)

init()
# for _ in range(int(input())):
solve()
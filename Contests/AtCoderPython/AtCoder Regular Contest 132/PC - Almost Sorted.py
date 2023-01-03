import collections
import functools
import math
import os
import random
import sys
# from functools import cache, reduce
from heapq import heappop, heappush
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

MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n, d = map(int, input().split())
    arr = ints()

    valid = [True] * n
    pos = [0]
    for i, a in enumerate(arr, 1):
        if a == -1:
            pos.append(i)
        else:
            valid[a-1] = False
    # print(pos)
    m = len(pos)
    if m == 1:
        print(1)
        return

    mx = 1 << d * 2 + 1
    vmask = mx - 1

    '''
    dp = [0] * mx
    dp[0] = 1
    for i in range(1, m):
        tmp = dp
        dp = [0] * mx
        l = max(0, d - pos[i] + 1)
        r = min(d * 2 + 1, d - pos[i] + n + 1)
        for mask in range(mx):
            if not tmp[mask]:
                continue
            cmask = (mask << (pos[i] - pos[i-1])) & vmask
            for j in range(l, r):
                k = pos[i] + j - d - 1
                if not valid[k] or (cmask >> (d * 2 - j)) & 1:
                    continue
                dp[cmask | (1 << (d * 2 - j))] += tmp[mask]
                dp[cmask | (1 << (d * 2 - j))] %= MOD

    print(sum(dp) % MOD)
    '''
    # @functools.cache
    # cache = [[-1] * (m + 1) for _ in range(mx)]
    # cache = dict()
    @functools.lru_cache(None)
    def go(mask, i) -> int:
        # print(f"F{mask:05b}", i)
        if i == m:
            return 1

        # if cache[mask][i] != -1:
        #     return cache[mask][i]
        # if (mask, i) in cache:
        #     return cache[(mask, i)]
        
        # omask = mask
        
        mask = (mask << (pos[i] - pos[i-1])) & vmask
        # print(f"T{mask:05b}", i)
        l = max(0, d - pos[i] + 1)
        r = min(d * 2 + 1, d - pos[i] + n + 1)
        # for j in range(d * 2 + 1):
        # print(l, r)
        res = 0
        for j in range(l, r):
            k = pos[i] + j - d - 1
            # print(k)
            if not valid[k] or (mask >> (d * 2 - j)) & 1:
                continue
            res += go(mask | (1 << (d * 2 - j)), i + 1)
            res %= MOD
        # cache[omask][i] = res
        # cache[(omask, i)] = res
        return res

    print(go(0, 1))

# t = int(input())
# for _ in range(t):
solve()
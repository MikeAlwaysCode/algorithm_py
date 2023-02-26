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

def solve() -> None:
    n = int(input())
    
    dp = [1, 1]
    pa, pb = map(int, input().split())
    for _ in range(n - 1):
        a, b = map(int, input().split())
        tmp = [0] * 2
        if a != pa:
            tmp[0] = (tmp[0] + dp[0]) % MOD
        if a != pb:
            tmp[0] = (tmp[0] + dp[1]) % MOD
        if b != pa:
            tmp[1] = (tmp[1] + dp[0]) % MOD
        if b != pb:
            tmp[1] = (tmp[1] + dp[1]) % MOD
        pa, pb = a, b
        dp = tmp
        # print(dp)
    print(sum(dp) % MOD)

    '''
    g = collections.defaultdict(list)
    vis = collections.Counter()

    for _ in range(n):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
        vis[a] = 0
        vis[b] = 0

    ans = 1
    # print(g)
    for v in vis.keys():
        if not vis[v] and g[v]:
            cntV = cntE = 0
            q = collections.deque([v])
            vis[v] = 1
            while q:
                u = q.popleft()
                cntV += 1
                cntE += len(g[u])
                for v in g[u]:
                    if not vis[v]: 
                        vis[v] = 1
                        q.append(v)
            # print(cntV, cntE)
            if cntE // 2 > cntV:
                print(0)
                return
            elif cntE // 2 < cntV:
                ans = ans * cntV % MOD
            elif cntV > 1:
                ans = ans * 2 % MOD
    print(ans)
    '''

solve()
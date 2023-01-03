import collections
import math
import os
import random
import sys
from functools import reduce
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
    n, k = map(int, input().split())

    # 阶乘
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i % MOD

    matrix = []
    for _ in range(n):
        matrix.append(ints())
    transpose = list(map(list, zip(*matrix)))
    
    def check(mat, i: int, j: int) -> bool:
        for l in range(n):
            if mat[i][l] + mat[j][l] > k:
                return False
        return True
    
    def cal(mat) -> int:
        fa = list(range(n))
        sz = [1] * n
        
        def find(x):
            cur = x
            while x != fa[x]:
                x = fa[x]
            if cur != x:
                fa[cur], cur = x, fa[x]
            return x
        
        for i in range(n):
            x = find(i)
            for j in range(i + 1, n):
                y = find(j)
                if y == x:
                    continue
                if check(mat, i, j):
                    fa[y] = x
                    sz[x] += sz[y]
                    sz[y] = 0
        
        res = 1
        for v in sz:
            if v > 0:
                res = (res * fact[v]) % MOD

        return res

    ans = (cal(matrix) * cal(transpose)) % MOD

    print(ans)

# t = int(input())
# for _ in range(t):
solve()
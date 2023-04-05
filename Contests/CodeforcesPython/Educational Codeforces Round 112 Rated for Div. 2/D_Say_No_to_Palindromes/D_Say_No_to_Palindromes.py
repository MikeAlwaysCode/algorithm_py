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
    n, m = map(int, input().split())
    s = input()
    
    per = list(itertools.permutations([0, 1, 2]))
    cnt = [[0] * (n + 1) for _ in range(6)]
    for i, c in enumerate(s):
        for j, p in enumerate(per):
            cnt[j][i + 1] = cnt[j][i]
            if p[ord(c) - 97] != i % 3 :
                cnt[j][i + 1] += 1
                    
    for _ in range(m):
        l, r = map(int, input().split())
        ans = r - l + 1
        for i in range(6):
            ans = min(ans, cnt[i][r] - cnt[i][l - 1])
        print(ans)
    '''
    per = [0, 1, 2]
    cnt = [[[0] * (n + 1) for _ in range(3)] for _ in range(3)]
    for i, c in enumerate(s):
        for j in range(3):
            for k in range(3):
                cnt[j][k][i + 1] = cnt[j][k][i]
                if ord(c) - 97 == j and i % 3 == k:
                    cnt[j][k][i + 1] += 1
                    
    for _ in range(m):
        l, r = map(int, input().split())
        ans = r - l + 1
        for p in itertools.permutations(per):
            c = r - l + 1
            for i, j in enumerate(p):
                c -= cnt[i][j][r] - cnt[i][j][l - 1]
            ans = min(ans, c)
        print(ans)
    '''

# for _ in range(int(input())):
solve()
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

# MOD = 998244353
# MOD = 10 ** 9 + 7
DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n = int(input())
    s = input()
    t = input()

    ans = 0
    ps = pt = -1
    while ps < n and pt < n:
        ps += 1
        pt += 1
        while ps < n and s[ps] == '1':
            ps += 1
        while pt < n and t[pt] == '1':
            pt += 1
        ans += ps != pt
    if ps < n or pt < n:
        print(-1)
    else:
        print(ans)

    '''
    spos = []
    tpos = []
    for i in range(n):
        if s[i] == '0':
            spos.append(i)
        if t[i] == '0':
            tpos.append(i)

    if len(spos) != len(tpos):
        print(-1)
        return
    
    m = len(spos)

    for i in range(m):
        if spos[i] != tpos[i]:
            ans += 1

    print(ans)
    '''
    # l, r = 0, m - 1
    # while l < m:
    #     if spos[l] != tpos[l]:
    #         if l < m - 1 and tpos[l] >= spos[l + 1]:
    #             break
    #         ans += 1
    #     l += 1

    # while r >= l: 
    #     if spos[r] != tpos[r]:
    #         if r > 0 and tpos[r] <= spos[r - 1]:
    #             break
    #         ans += 1
    #     r -= 1
    
    # if r >= l:
    #     print(-1)
    #     return

# t = int(input())
# for _ in range(t):
solve()
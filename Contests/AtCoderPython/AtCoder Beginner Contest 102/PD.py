import collections
import math
import os
import random
import sys
from functools import reduce
from heapq import heappop, heappush
from io import BytesIO, IOBase
from itertools import accumulate

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
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n = int(input())
    arr = ints()

    # pres = list(accumulate(arr, initial=0))
    pres = [0] + list(accumulate(arr))

    def bs(pl: int, pr: int):
        tot = pres[pr] - pres[pl]
        l, r = pl, pr
        while l <= r:
            mid = l + r >> 1
            ls = pres[mid] - pres[pl]
            if ls * 2 == tot:
                return (ls, ls, ls, ls)
            elif ls * 2 > tot:
                r = mid - 1
            else:
                l = mid + 1

        return (pres[r] - pres[pl], pres[pr] - pres[r], pres[l] - pres[pl], pres[pr] - pres[l])

    def cal(a, b, c, d):
        return max(a, b, c, d) - min(a, b, c, d)

    ans = pres[-1]
    # for i in range(1, n - 2):

    #     (a1, b1, a2, b2) = bs(0, i + 1)
    #     (c1, d1, c2, d2) = bs(i + 1, n)

    #     r = min(cal(a1, b1, c1, d1), cal(a2, b2, c1, d1), cal(a1, b1, c2, d2), cal(a2, b2, c2, d2))

    #     ans = min(ans, r)
    
    l, m, r = 1, 2, 3
    while m < n - 1:
        mids = pres[m]
        while abs(pres[l] * 2 - mids) > abs(pres[l+1] * 2 - mids):
            l += 1
            
        while abs(pres[r] * 2 - mids - pres[n]) > abs(pres[r+1] * 2 - mids - pres[n]):
            r += 1

        a, b, c, d = pres[l], mids - pres[l], pres[r] - mids, pres[n] - pres[r]
        ans = min(ans, cal(a, b, c, d))

        m += 1

    print(ans)

# t = int(input())
# for _ in range(t):
solve()
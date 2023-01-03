import math
import collections
import random
from heapq import heapify, heappush, heappop
from functools import reduce
from bisect import bisect, bisect_left

# Sample Inputs/Output 
# region fastio
import sys, os
from io import BytesIO, IOBase
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

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)


def solve() -> None:
    n, w = map(int, input().split())

    # Log Prepare
    MX = w + 2
    logn = [0] * (MX)
    logn[1] = 0
    for i in range(2, MX):
        logn[i] = logn[i//2] + 1
    st = [[0] * 22 for _ in range(MX)]

    ans = [0] * (w + 2)
    for _ in range(n):
        arr = ints()
        l = arr[0]
        if 2 * l <= w:
            pre = suf = 0
            for i in range(1, l + 1):
                pre = max(pre, arr[i])
                suf = max(suf, arr[-i])
                ans[i] += pre
                ans[i + 1] -= pre
                ans[w - i + 1] += suf
                ans[w - i + 2] -= suf
            ans[l + 1] += pre
            ans[w - l + 1] -= pre
        else:
            for i in range(1, l + 1):
                st[i][0] = arr[i]

            for j in range(1, logn[l] + 1):
                for i in range(1, l - (1<<j) + 2):
                    st[i][j] = max(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
                    
            for j in range(1, w + 1):
                left = l - w + j
                right = j
                ll = max(left, l)
                rr = min(right, l)
                k = logn[rr - ll + 1]
                v = max(st[ll][k], st[rr - (1 << k) + 1][k])
                if left < l or right > l:
                    v = max(0, v)
                ans[j] += v
                ans[j + 1] -= v
        print(ans)
    print(ans)
    for i in range(1, w + 1):
        ans[i] += ans[i-1]
    print(*ans[1:w + 1])

# t = int(input())
# for _ in range(t):
solve()
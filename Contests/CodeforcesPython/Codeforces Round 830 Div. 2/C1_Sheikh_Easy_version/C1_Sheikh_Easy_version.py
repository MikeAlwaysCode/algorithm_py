from itertools import accumulate
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
    n, q = map(int, input().split())
    arr = ints()
    pres = [0] * (n + 1)
    xor = [0] * (n + 1)

    for i, a in enumerate(arr):
        pres[i+1] = pres[i] + a
        xor[i+1] = xor[i] ^ a

    # print(pres)
    # print(xor)

    def cal(l, r) -> int:
        return pres[r] - pres[l] - (xor[r] ^ xor[l])

    for _ in range(q):
        L, R = map(int, input().split())
        ansl, ansr = L, R
        mx = cal(L-1, R)
        for i in range(L-1, R):
            cur = cal(i, R)
            # print("to", i, cur)
            if cur < mx:
                continue
            l, r = i + 1, R
            while l < r:
                mid = (l + r) >> 1
                if cal(i, mid) < cur:
                    l = mid + 1
                else:
                    r = mid
            # print("res", cur, i, l)
            if cur > mx or (cur == mx and l - i - 1 < ansr - ansl):
                mx = cur
                ansl, ansr = i + 1, l

        print(ansl, ansr)

t = int(input())
for _ in range(t):
    solve()
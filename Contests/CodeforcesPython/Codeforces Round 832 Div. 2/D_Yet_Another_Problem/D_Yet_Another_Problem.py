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
    xor = [0] * (n + 1)
    pres = [0] * (n + 1)
    left = [-1] * (n + 1)
    odd = dict()
    even = dict()

    for i in range(n):
        xor[i+1] = xor[i] ^ arr[i]
        pres[i+1] = pres[i] + arr[i]
        if i & 1:
            if xor[i+1] in odd:
                left[i+1] = odd[xor[i+1]]
            even[xor[i+1]] = i + 1
        else:
            if xor[i+1] in even:
                left[i+1] = even[xor[i+1]]
            odd[xor[i+1]] = i + 1

    for _ in range(q):
        l, r = map(int, input().split())
        if pres[r] - pres[l-1] == 0:
            print(0)
        elif xor[r] ^ xor[l-1] == 0:
            if (r - l + 1) & 1:
                print(1)
            elif arr[r-1] == 0 or arr[l-1] == 0:
                print(1)
            elif left[r] >= l:
                print(2)
            else:
                print(-1)
        else:
            print(-1)
    # print(arr)
    # print(xor)
    # print(pres)

# t = int(input())
# for _ in range(t):
solve()
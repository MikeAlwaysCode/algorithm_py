from itertools import accumulate
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

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

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n, k = map(int, input().split())
    arr = ints()

    left = [0] * n
    right = [0] * n
    pres = pren = 0
    for i in range(0, k - 1):
        pres += arr[i]
        pren += arr[i]
        if pren >= 0:
            pren = 0

        left[i] = min(pres, pren)
    pres = pren = 0
    for i in range(n - 1, k - 1, -1):
        pres += arr[i]
        pren += arr[i]
        if pren >= 0:
            pren = 0
            
        right[i] = min(pres, pren)

    # print(left)
    # print(right)
    s = set([(k - 2, k)])
    q = [(arr[k-1], k - 2, k)]
    while q:
        tmp = q
        q = []
        for h, l, r in tmp:
            # if h >= left[l] or h >= right[n-r]:
            # if l == -1 or r == n:
            if l == -1 or r == n or h + left[l] >= 0 or h + right[r] >= 0:
                # print(l, r)
                print("YES")
                return
            if h + arr[l] >= 0 and (l - 1, r) not in s:
                s.add((l - 1, r))
                q.append((h + arr[l], l - 1, r))
            if h + arr[r] >= 0 and (l, r + 1) not in s:
                s.add((l, r + 1))
                q.append((h + arr[r], l, r + 1))
    print("NO")

t = int(input())
for _ in range(t):
    solve()
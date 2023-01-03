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
    n = int(input())
    arr = ints()

    tot = 0
    mx = 0
    for i in range(n-1, -1, -1):
        mx += abs(arr[i])
        if i & 1:
            tot -= arr[i]
        else:
            tot += arr[i]

    if tot == 0:
        print(1)
        print(1, n)
        return

    if mx & 1:
        print(-1)
        return
    ans = []
    cur = 0
    pre = n
    for i in range(n-1, -1, -1):
        if i & 1:
            cur -= arr[i]
            if tot * cur > 0:
                if abs(tot) >= abs(cur * 2):
                    tot -= 2 * cur
                    ans.append((i + 1, pre))
                else:
                    tot += 2 * arr[i]
                    ans.append((i + 2, pre))
                    ans.append((i + 1, i + 1))
                cur = 0
                pre = i
                if tot == 0:
                    break
        else:
            cur += arr[i]
    if tot != 0:
        print(-1)
        return

    ans.append((1, pre))
    ans.sort()

    print(len(ans))
    for x, y in ans:
        print(x, y)

t = int(input())
for _ in range(t):
    solve()
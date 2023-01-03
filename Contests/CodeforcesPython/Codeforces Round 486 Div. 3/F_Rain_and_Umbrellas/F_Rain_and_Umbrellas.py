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

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    a, n, m = map(int, input().split())
    rain = []
    umbrella = []
    for _ in range(n):
        l, r = map(int, input().split())
        rain.append((l, r))
    for _ in range(m):
        x, p = map(int, input().split())
        umbrella.append((x, p))
        
    rain.sort()
    umbrella.sort()
    if umbrella[0][0] > rain[0][0]:
        print(-1)
        return
    
    umbrella.append((a, 0))
    dp = [math.inf] * (m + 1)
    dp[0] = 0
    k = -1
    for i, (x, c) in enumerate(umbrella):
        while k + 1 < n and rain[k+1][0] < x:
            k += 1
        
        if k < 0:
            if i > 0:
                dp[i] = dp[i-1]
            continue

        x = min(x, rain[k][1])
        if umbrella[i-1][0] >= x:
            dp[i] = dp[i-1]
            continue

        for j, q in enumerate(umbrella[:i]):
            dp[i] = min(dp[i], dp[j] + (x - q[0]) * q[1])
    
    print(dp[m])

# t = int(input())
# for _ in range(t):
solve()
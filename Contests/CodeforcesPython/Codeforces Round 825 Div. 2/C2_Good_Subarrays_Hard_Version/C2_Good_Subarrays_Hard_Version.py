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

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

class segtree:
    def __init__(self , n , function , bound):
        self.st = [bound] * (2 * n)
        self.size = n
        self.function = function
        self.bound = bound

    def update(self , x , value):
        x += self.size
        self.st[x] = value
        while(x > 1):
            x >>= 1
            self.st[x] = self.function(self.st[2 * x] , self.st[2 * x + 1])

    def query(self , x , y):
        x += self.size
        y += self.size + 1

        ans = self.bound
        while(x < y):
            if(x & 1):
                ans = self.function(ans , self.st[x])
                x += 1
            if(y & 1):
                y -= 1
                ans = self.function(ans , self.st[y])

            x //= 2
            y //= 2
        return ans

def solve() -> None:
    n = int(input())
    arr = ints()

    dp = [0] * n
    pref = [0] * n
    track = []
    pres = list(accumulate(range(n)))
    dp[0] = pref[0] = 1
    for i in range(1, n):
        dp[i] = min(arr[i], dp[i-1] + 1)
        pref[i] = pref[i-1] + dp[i]
        track.append((arr[i] - i - 1, i + 1, 0))
    
    q = int(input())
    ans = [0] * q
    for i in range(q):
        p, x = map(int, input().split())
        x = min(dp[p-1] + 1, x)
        track.append((x - p, p, i))
    

# t = int(input())
# for _ in range(t):
solve()
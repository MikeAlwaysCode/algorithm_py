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
    q = int(input())
    a = [[0] * 26 for _ in range(2)]
    a[0][0] = a[1][0] = 1
    for _ in range(q):
        d, k, s = input().split()
        for x in s:
            a[int(d)-1][ord(x)-97] += int(k)
        
        i, j = 0, 25
        while i < 26 or j >= 0:
            while i < 26 and not a[0][i]:
                i += 1
            while j >= 0 and not a[1][j]:
                j -= 1

            if j < 0:
                print("NO")
                break
            elif i >= 26:
                print("YES")
                break
            
            if i == j:
                if a[0][i] == a[1][j]:
                    i += 1
                    j -= 1
                    continue
                if a[0][i] < a[1][j]:
                    i += 1
                    continue
                else:
                    j -= 1
                    continue
                
            if i < j:
                print("YES")
                break
            else:
                print("NO")
                break

t = int(input())
for _ in range(t):
    solve()
import copy
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
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(ints())
    cur = copy.deepcopy(grid)
    cnt = [n] * m
    # cnt = n * m

    k = int(input())
    shoot = [False] * k
    res = [0] * k
    # last = 0
    for i in range(k):
        arr = ints()
        if arr[0] == 1:
            # shoot.append([i, 0])
            shoot[i] = True
            # last = i
        else:
            if cur[arr[1]-1][arr[2]-1] == grid[arr[1]-1][arr[2]-1] and arr[3] != grid[arr[1]-1][arr[2]-1]:
                cnt[arr[2]-1] -= 1
                # cnt -= 1
            elif cur[arr[1]-1][arr[2]-1] != grid[arr[1]-1][arr[2]-1] and arr[3] == grid[arr[1]-1][arr[2]-1]:
                cnt[arr[2]-1] += 1
                # cnt += 1

            cur[arr[1]-1][arr[2]-1] = arr[3]

        # for j in range(len(shoot)):
        #     if i - shoot[j][0] < m:
        #         shoot[j][1] += cnt[i - shoot[j][0]]
        for j in range(max(0, i-m+1), i+1):
            res[j] += cnt[i-j]
    
    # print(res)
    for j in range(max(0, k-m+1), k):
        res[j] += cnt[m-k+j-1]
        
    # print(shoot)
    ans = 0
    # print(res)
    for i, (r, s) in enumerate(zip(res, shoot)):
        if s:
            ans = max(ans, r)

    print(ans)

# t = int(input())
# for _ in range(t):
solve()
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
    ans = [[-1] * n for _ in range(n)]
    ans[0][0] = 0

    dir = []
    # k = math.isqrt(m)
    k = int(math.sqrt(m))
    while k > 0:
        if k * k == m:
            dir.append((k, 0))
            dir.append((-k, 0))
            dir.append((0, k))
            dir.append((0, -k))
        else:
            mk = m - k * k
            # l = math.isqrt(mk)
            l = int(math.sqrt(mk))
            if l * l == mk:
                dir.append((k, l))
                dir.append((-k, l))
                dir.append((k, -l))
                dir.append((-k, -l))

        k -= 1

    def check(x, y):
        if 0 <= x < n and 0 <= y < n:
            return True
        else:
            return False

    # print(dir)

    q = [(0, 0, 0)]
    while q:
        tmp = q
        q = []
        for x, y, op in tmp:
            for dr, dc in dir:
                nx = x + dr
                ny = y + dc
                if check(nx, ny):
                    if ans[nx][ny] < 0:
                        ans[nx][ny] = op + 1
                        q.append((nx, ny, op+1))
                    elif op + 1 < ans[nx][ny]:
                        ans[nx][ny] = op + 1
                        q.append((nx, ny, op+1))
    
    for i in range(n):
        print(*ans[i])

# t = int(input())
# for _ in range(t):
solve()
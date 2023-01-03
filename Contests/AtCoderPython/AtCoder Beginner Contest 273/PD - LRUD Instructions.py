from bisect import bisect
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
    h, w, x, y = map(int, input().split())
    # grid = [[0] * w for _ in range(h)]
    # row = [[] for _ in range(h+1)]
    # col = [[] for _ in range(w+1)]
    row = collections.defaultdict(list)
    col = collections.defaultdict(list)

    n = int(input())
    wall = []
    for _ in range(n):
        r, c = map(int, input().split())
        wall.append((r, c))
        # grid[r-1][c-1] = 1
    
    wall.sort(key = lambda x: x[1])
    for i in range(n):
        row[wall[i][0]].append(wall[i][1])
    wall.sort()
    for i in range(n):
        col[wall[i][1]].append(wall[i][0])

    q = int(input())

    ly = ry = lx = rx = 0

    def update(d, nx, ny):
        nonlocal ly, ry, lx, rx
        if d == "L":
            if row[nx]:
                idx = bisect(row[nx], ny)
                if idx == 0:
                    ly = 1
                else:
                    ly = row[nx][idx-1] + 1
            else:
                ly = 1
        elif d == "R":
            if row[nx]:
                idx = bisect(row[nx], ny)
                if idx == len(row[nx]):
                    ry = w
                else:
                    ry = row[nx][idx] - 1
            else:
                ry = w
        elif d == "U":
            if col[ny]:
                idx = bisect(col[ny], nx)
                if idx == 0:
                    lx = 1
                else:
                    lx = col[ny][idx-1] + 1
            else:
                lx = 1
        elif d == "D":
            if col[ny]:
                idx = bisect(col[ny], nx)
                if idx == len(col[ny]):
                    rx = h
                else:
                    rx = col[ny][idx] - 1
            else:
                rx = h
    
    ans = []
    pred = ""
    for i in range(q):
        d, l = input().split()
        l = int(l)

        if d != pred:
            update(d, x, y)
            pred = d

        if d == "L":
            ny = max(ly, y - l)
            y = ny
        elif d == "R":
            ny = min(ry, y + l)
            y = ny
        elif d == "U":
            nx = max(lx, x - l)
            x = nx
        elif d == "D":
            nx = min(rx, x + l)
            x = nx

        ans.append((x, y))
    
    for i in range(q):
        print(*ans[i])

# t = int(input())
# for _ in range(t):
solve()
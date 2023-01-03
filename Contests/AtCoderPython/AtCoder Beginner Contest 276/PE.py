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
    n, m = map(int, input().split())
    grid = []
    xs = ys = -1
    for i in range(n):
        grid.append(input())
        
        if xs == -1 and grid[-1].find('S') >= 0:
            xs, ys = i, grid[-1].find('S')
    
    DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))
    visit = [[0] * m for _ in range(n)]
    q = collections.deque([(xs, ys)])
    idx = 0
    while q:
        (x, y) = q.popleft()
        for dr, dc in DIR:
            nx, ny = x + dr, y + dc
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.':
                if x == xs and y == ys:
                    idx += 1
                    visit[nx][ny] = idx
                    q.append((nx, ny))
                elif visit[nx][ny] != 0 and visit[nx][ny] != visit[x][y]:
                    print("Yes")
                    return
                elif visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y]
                    q.append((nx, ny))

    print("No")

# t = int(input())
# for _ in range(t):
solve()
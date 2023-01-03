import math
import collections
import random
from heapq import heapify, heappush, heappop
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
    n = int(input())
    arr = ints()

    mn, mx = 0, n
    if arr[0] > n:
        k = n
    else:
        k = 0
    incnt = [0] * (n + 1)
    edge = [[] for _ in range(n + 1)]
    for i, a in enumerate(arr):
        if a == n + 1:
            mn = max(mn, i + 1)
        elif a == 0:
            mx = min(mx, i)
        else:
            if a > i + 1:
                mn = max(mn, i + 1)
                mx = min(mx, a - 1)
            else:
                mn = max(mn, a)
                mx = min(mx, i)
            incnt[i + 1] += 1
            edge[a].append(i + 1)
        if mn == mx:
            k = mn

    # topoSort()
    # q = collections.deque((len(edge[i]), i) for i, v in enumerate(incnt) if i > 0 and v == 0)
    q = [(len(edge[i]), i) for i, v in enumerate(incnt) if i > 0 and v == 0]
    heapify(q)
    ans = [0] * n
    cnt = 0
    while q:
        pair = heappop(q)
        cur = pair[1]

        ans[cnt] = cur
        cnt += 1
        
        for x in edge[cur]:
            incnt[x] -= 1
            if incnt[x] == 0:
                # q.append(x)
                heappush(q, (len(edge[x]), x))

    print(k)
    print(*ans)

t = int(input())
for _ in range(t):
    solve()
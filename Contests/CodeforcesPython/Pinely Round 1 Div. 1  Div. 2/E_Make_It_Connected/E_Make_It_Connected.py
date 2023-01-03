import collections
import math
import os
import random
import sys
from bisect import bisect, bisect_left
from functools import reduce
from heapq import heapify, heappop, heappush
from io import BytesIO, IOBase

# Sample Inputs/Output 
# region fastio
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
DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(input())
    
    visited = [False] * n

    ans = n
    res = []
    clique = []
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        con = []
        q = collections.deque([i])
        while q:
            x = q.popleft()
            cnt = 0
            for j in range(n):
                if matrix[x][j] == '1':
                    cnt += 1
                    if not visited[j]:
                        q.append(j)
                        visited[j] = True
            con.append((cnt, x + 1))

        if len(con) == n:
            print(0)
            return

        con.sort()
        if con[0][0] == len(con) - 1:
            cur = len(con)
            _, cres = map(list, zip(*con))
            clique.append(cres[0])
        else:
            cur = 1
            cres = [con[0][1]]

        if cur < ans:
            ans = cur
            res = cres
        if ans == 1:
            break
    
    # If there are exactly 2 connected components, 
    # then apparently we will have to operate on all vertices in a connected component. 
    # So we'll choose the smaller connected component to operate, 
    # and the answer is exactly the size of it.
    # Otherwise, we can arbitrarily choose two vertices 
    # from two different connected components and operate on them. 
    # The answer is 2.
    if ans > 1 and len(clique) > 2:
        ans = 2
        res = clique[:2]

    print(ans)
    print(*res)

t = int(input())
for _ in range(t):
    solve()
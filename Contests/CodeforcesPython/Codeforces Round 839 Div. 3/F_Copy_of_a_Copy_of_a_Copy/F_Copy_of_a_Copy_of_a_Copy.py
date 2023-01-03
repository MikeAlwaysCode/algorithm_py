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
# endregion fastio

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, m, k = map(int, input().split())
    matrix = [[] for _ in range(k + 1)]
    for i in range(k + 1):
        input()
        for _ in range(n):
            matrix[i].append(input())
 
    op = collections.defaultdict(list)
 
    def check(i, j) -> bool:
        top = []
        for x in range(1, n - 1):
            for y in range(1, m - 1):
                if matrix[i][x][y] != matrix[j][x][y]:
                    if matrix[i][x - 1][y] != matrix[j][x - 1][y] \
                        or matrix[i][x][y - 1] != matrix[j][x][y - 1] \
                        or matrix[i][x + 1][y] != matrix[j][x + 1][y] \
                        or matrix[i][x][y + 1] != matrix[j][x][y + 1] \
                        or matrix[i][x][y] == matrix[i][x - 1][y] \
                        or matrix[i][x][y] == matrix[i][x][y - 1] \
                        or matrix[i][x][y] == matrix[i][x + 1][y] \
                        or matrix[i][x][y] == matrix[i][x][y + 1]:
                        return False
                    top.append((1, x + 1, y + 1))
        op[(i, j)] = top
        return True
 
    indgrees = [0] * (k + 1)
    edge = [set() for _ in range(k + 1)]
    for i in range(k + 1):
        for j in range(k + 1):
            if i == j: continue
            if i in edge[j]: continue
            if check(i, j):
                indgrees[j] += 1
                # edge[i].append(j)
                edge[i].add(j)
    
    # print(indgrees)
    # print(edge)
    # print(op)
    
    # seen = set()
    # def dfs(x) -> bool:
    #     path.append(x)
    #     seen.add(x)
    #     if len(path) == k + 1:
    #         return True
    #     for y in edge[x]:
    #         if y in seen: continue
    #         if dfs(y): return True
    #     seen.remove(x)
    #     path.pop()
    #     return False
 
    # for i in range(k + 1):
    #     if dfs(i):
    #         break
 
    path = []
    q = collections.deque(i for i, v in enumerate(indgrees) if v == 0)
    while q:
        x = q.popleft()
        path.append(x)
        for y in edge[x]:
            indgrees[y] -= 1
            if indgrees[y] == 0:
                q.append(y)

    # print(path)
    print(path[0] + 1)
    ans = []
    for i in range(1, len(path)):
        pre = path[i - 1]
        nxt = path[i]
        ans.extend(op[(pre, nxt)])
        ans.append((2, nxt + 1))
 
    print(len(ans))
    for o in ans:
        print(*o)

# t = int(input())
t = 1
for _ in range(t):
    solve()
import itertools
import math
import os
import random
import sys
from bisect import bisect, bisect_left
from collections import *
from functools import reduce
from heapq import heapify, heappop, heappush
from io import BytesIO, IOBase
from string import *

# region fastio
# BUFSIZE = 8192
# class FastIO(IOBase):
#     newlines = 0

#     def __init__(self, file):
#         self._fd = file.fileno()
#         self.buffer = BytesIO()
#         self.writable = "x" in file.mode or "r" not in file.mode
#         self.write = self.buffer.write if self.writable else None

#     def read(self):
#         while True:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             if not b:
#                 break
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines = 0
#         return self.buffer.read()

#     def readline(self):
#         while self.newlines == 0:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             self.newlines = b.count(b"\n") + (not b)
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines -= 1
#         return self.buffer.readline()

#     def flush(self):
#         if self.writable:
#             os.write(self._fd, self.buffer.getvalue())
#             self.buffer.truncate(0), self.buffer.seek(0)

# class IOWrapper(IOBase):
#     def __init__(self, file):
#         self.buffer = FastIO(file)
#         self.flush = self.buffer.flush
#         self.writable = self.buffer.writable
#         self.write = lambda s: self.buffer.write(s.encode("ascii"))
#         self.read = lambda: self.buffer.read().decode("ascii")
#         self.readline = lambda: self.buffer.readline().decode("ascii")
        
# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))
# endregion fastio

# region interactive
def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)
# endregion interactive

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        
    parent = [-1] * n
    order = [0]
    stack = [0]
    while stack:
        u = stack.pop()
        for v in g[u]:
            if v == parent[u]: continue
            parent[v] = u
            order.append(v)
            stack.append(v)
    
    seen = dict()
    hash_val = [0] * n
    idx = 0

    for u in order[::-1]:
        children = []
        for v in g[u]:
            if v == parent[u]: continue
            children.append(hash_val[v])
        code = tuple(sorted(children))
        if code not in seen:
            idx += 1
            seen[code] = idx
        hash_val[u] = seen[code]

    u = 0
    while True:
        cnt = Counter()
        for v in g[u]:
            if v == parent[u]: continue
            cnt[hash_val[v]] += 1
        c = 0
        for v in cnt.values():
            if v & 1: c += 1
        
        if c == 0:
            print("YES")
            return
        if c > 1:
            print("NO")
            return
        
        for v in g[u]:
            if v == parent[u]: continue
            if cnt[hash_val[v]] & 1:
                u = v
                break

for _ in range(int(input())):
    solve()
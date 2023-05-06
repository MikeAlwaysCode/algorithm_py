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

# region interactive
def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)
# endregion interactive

# from types import GeneratorType
# def bootstrap(f, stack=[]):
#     def wrappedfunc(*args, **kwargs):
#         if stack:
#             return f(*args, **kwargs)
#         else:
#             to = f(*args, **kwargs)
#             while True:
#                 if type(to) is GeneratorType:
#                     stack.append(to)
#                     to = next(to)
#                 else:
#                     stack.pop()
#                     if not stack:
#                         break
#                     to = stack[-1].send(to)
#             return to
#     return wrappedfunc

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    m, n = map(int, input().split())
    p = ints()
    rating = []
    for _ in range(m):
        rating.append(ints())

    g = [set() for _ in range(n)]
    idx = list(range(n))
    idx.sort(key = lambda x: rating[0][x])
    s = set()
    k = n - 1
    for i in range(n - 1, -1, -1):
        j = idx[i]
        while k > i and rating[0][idx[k]] > rating[0][j]:
            s.add(idx[k])
            k -= 1
        g[j] = s.copy()
    
    for i in range(1, m):
        # idx.sort(key = lambda x: rating[i][x])
        # s.clear()
        # k = n - 1
        # for l in range(n - 1, -1, -1):
        #     j = idx[l]
        #     while k > l and rating[i][idx[k]] > rating[i][j]:
        #         s.add(idx[k])
        #         k -= 1
        #     g[j] &= s
        for j in range(n):
            for k in g[j].copy():
                if rating[i][j] >= rating[i][k]:
                    g[j].remove(k)

    ans = 0
    val = [0] * n

    for i in range(n):
        if val[i]: continue
        
        val[i] = p[i]
        q = [(- val[i], i)]
        while q:
            v, x = heappop(q)
            v = -v
            ans = max(ans, v)
            for y in g[x]:
                if val[y] >= v + p[y]: continue
                val[y] = val[x] + p[y]
                heappush(q, (- val[y], y))
    
    print(ans)

# for _ in range(int(input())):
solve()
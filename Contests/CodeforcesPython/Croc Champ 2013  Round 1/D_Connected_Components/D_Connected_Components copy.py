# import math
import os
import sys
# from bisect import *
# from collections import *
# from copy import copy
# from functools import *
# from heapq import *
from io import BytesIO, IOBase

# from itertools import *
# from random import *
# from string import *
# from types import GeneratorType

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
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))
# endregion fastio

# # region interactive
# def printQry(a, b) -> None:
#     sa = str(a)
#     sb = str(b)
#     print(f"? {sa} {sb}", flush = True)

# def printAns(ans) -> None:
#     s = str(ans)
#     print(f"! {s}", flush = True)
# # endregion interactive

# # region dfsconvert
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
# # endregion dfsconvert

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

class UnionFind:
    def __init__(self, n: int) -> None:
        self.fa = list(range(n))
        self.rank = [0] * n
        self.set_count = n

    def find(self, x: int) -> int:
        cur = x
        while x != self.fa[x]:
            x = self.fa[x]
        # while fa[cur] != x:
            # tmp = fa[cur]
            # fa[cur] = x
            # cur = tmp
        while cur != x:
            self.fa[cur], cur = x, self.fa[cur]
        return x
    
    def union(self, x: int, y: int):
        x, y = self.find(x), self.find(y)
        if x == y: return
        # if x < y: x, y = y, x
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        elif self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        # rank[x] += rank[y]
        self.fa[y] = x
        self.set_count -= 1

def solve() -> None:
    n, m = mint()

    uf = UnionFind(n)
    # pres = [(fa.copy(), rank.copy(), set_count)]
    # pres = [(copy(fa), copy(rank), set_count)]
    # pres = [deepcopy(uf)]
    # pres = [(copy(uf.fa), copy(uf.rank), uf.set_count)]
    pres = [(uf.fa[:], uf.rank[:], uf.set_count)]
    edges = []
    # edges = inp_2ds(int, m)
    for _ in range(m):
        u, v = mint()
    # for u, v in edges:
        u -= 1
        v -= 1
        edges.append((u, v))
        uf.union(u, v)
        # pres.append((fa[:], rank[:], set_count))
        # pres.append((copy(fa), copy(rank), set_count))
        # pres.append(deepcopy(uf))
        # pres.append((copy(uf.fa), copy(uf.rank), uf.set_count))
        pres.append((uf.fa[:], uf.rank[:], uf.set_count))
    
    suf_uf = UnionFind(n)
    suff = [suf_uf.fa[:]]
    for u, v in reversed(edges):
    # for u, v in edges[::-1]:
        suf_uf.union(u, v)
        # suff.append(fa[:])
        suff.append(suf_uf.fa[:])
    
    for _ in range(sint()):
        l, r = mint()
        r = m - r
        
        uf.fa, uf.rank, uf.set_count = pres[l - 1][0][:], pres[l - 1][1][:], pres[l - 1][2]
        # fa, rank, set_count = copy(pres[l - 1][0]), copy(pres[l - 1][1]), pres[l - 1][2]
        # uf = deepcopy(pres[l - 1])
        # uf.fa, uf.rank, uf.set_count = copy(pres[l - 1][0]), copy(pres[l - 1][1]), pres[l - 1][2]
        for i, x in enumerate(suff[r]):
            uf.union(uf.fa[i], uf.fa[x])

        print(uf.set_count)

# for _ in range(int(input())):
solve()
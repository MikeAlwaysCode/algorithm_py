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
# input = lambda: sys.stdin.readline().rstrip("\r\n")
input = lambda: sys.stdin.readline().rstrip()
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
    n = int(input())
    arr = ints()
    
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)
    
    c=[(arr[i]<<20) + i for i in range(n)]
    c.sort()
    mask=(1<<20) - 1
    
    def f1() -> int:
        res = 0

        fa = list(range(n))
        sz = [1] * n

        def find(x: int):
            cur = x
            while x != fa[x]:
                x = fa[x]
            while fa[cur] != x:
                tmp = fa[cur]
                fa[cur] = x
                cur = tmp
            return x

        def union(fr: int, to: int):
            # fa[find(fr)] = find(to)
            fa[fr] = to
            sz[to] += sz[fr]

        for cv in c:
            av = cv >> 20
            v = cv & mask
            cnt1 = cnt2 = 0
            for u in edge[v]:
                if arr[u] < av or (arr[u] == av and u < v):
                    fu = find(u)
                    cnt1 += sz[fu]
                    cnt2 += sz[fu]**2
                    union(fu, find(v))
            res += av*(2*cnt1+cnt1**2-cnt2)

        return res
    
    def f2() -> int:
        res = 0

        fa = list(range(n))
        sz = [1] * n

        def find(x: int):
            cur = x
            while x != fa[x]:
                x = fa[x]
            while fa[cur] != x:
                tmp = fa[cur]
                fa[cur] = x
                cur = tmp
            return x

        def union(fr: int, to: int):
            # fa[find(fr)] = find(to)
            fa[fr] = to
            sz[to] += sz[fr]

        for cv in c[::-1]:
            av = cv >> 20
            v = cv & mask
            cnt1 = cnt2 = 0
            for u in edge[v]:
                if arr[u] > av or (arr[u] == av and u > v):
                    fu = find(u)
                    cnt1 += sz[fu]
                    cnt2 += sz[fu]**2
                    union(fu, find(v))
            res += av*(2*cnt1+cnt1**2-cnt2)

        return res

    print((f1() - f2()) // 2)

    '''
    # Case 37 TLE
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        if arr[u] > arr[v]:
            u, v = v, u
        edges.append((u, v))

    def dsu(p) -> int:
        res = 0

        fa = list(range(n))
        sz = [1] * n

        def find(x: int):
            cur = x
            while x != fa[x]:
                x = fa[x]
            while fa[cur] != x:
                tmp = fa[cur]
                fa[cur] = x
                cur = tmp
            return x

        def union(fr: int, to: int):
            # fa[find(fr)] = find(to)
            fa[fr] = to
            sz[to] += sz[fr]

        for e in edges:
            fu = find(e[0])
            fv = find(e[1])
            res += arr[e[p]] * sz[fu] * sz[fv]
            union(fu, fv)

        return res
    
    # 计算最大值的贡献，把最大值从小到大排序
    edges.sort(key = lambda x: arr[x[1]])
    ans = dsu(1)
    # 计算最小值的贡献，把最小值从大到小排序
    edges.sort(key = lambda x: -arr[x[0]])
    ans -= dsu(0)
    print(ans)
    '''

# for _ in range(int(input())):
solve()
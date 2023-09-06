import sys

# import itertools
# import math
import os
# import random
# from bisect import bisect, bisect_left
# from collections import *
# from functools import reduce
# from heapq import heapify, heappop, heappush
from io import BytesIO, IOBase
# from string import *

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
# print = lambda d: sys.stdout.write(str(d) + "\n")
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
# # endregion dfsconvert

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, q = mint()
    nums = ints()
    left = []
    right = []
    for _ in range(q):
        l, r = mint()
        left.append(l - 1)
        right.append(r)
    
    qi = list(range(q))
    '''
    block_size = int(1.4 * n // (int(q ** 0.5) + 1)) + 1
    qi.sort(key = lambda x: (right[x] // block_size, left[x] * (-1) ** (right[x] // block_size)))
    '''
    block_size = int(n ** 0.5)
    qi.sort(key = lambda x: ((left[x] - 1) // block_size + 1, right[x]))

    # ans = [0] * q
    ans = [None] * q
    curr = l = r = 0
    cnt = [0] * (10 ** 6 + 1)

    def add(x: int):
        nonlocal curr
        x = nums[x]
        curr += x * (2 * cnt[x] + 1)
        cnt[x] += 1
    
    def delete(x: int):
        nonlocal curr
        x = nums[x]
        cnt[x] -= 1
        curr -= x * (2 * cnt[x] + 1)

    for i in qi:
        nl, nr = left[i], right[i]
        while r < nr:
            add(r)
            r += 1
        while nr < r:
            r -= 1
            delete(r)
        while nl < l:
            l -= 1
            add(l)
        while l < nl:
            delete(l)
            l += 1
        ans[i] = curr

    # for v in ans:
    #     print(v)
    print(*ans, sep = "\n")

solve()
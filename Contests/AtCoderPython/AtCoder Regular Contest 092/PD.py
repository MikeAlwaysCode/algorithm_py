from io import BytesIO, IOBase
import random
import sys
import os

import bisect
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from itertools import accumulate, combinations, permutations
from operator import add, iand, ior, itemgetter, mul, xor
from string import ascii_lowercase, ascii_uppercase
from typing import *
BUFSIZE = 4096

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

sys.stdin = IOWrapper(sys.stdin)
sys.stdout = IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

def I():
    return input()

def II():
    return int(input())

def MII():
    return map(int, input().split())

def LI():
    return list(input().split())

def LII():
    return list(map(int, input().split()))

def GMI():
    return map(lambda x: int(x) - 1, input().split())

def LGMI():
    return list(map(lambda x: int(x) - 1, input().split()))

inf = float('inf')

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

# RANDOM = random.getrandbits(32)

# class Wrapper(int):
#     def __init__(self, x):
#         int.__init__(x)

#     def __hash__(self):
#         return super(Wrapper, self).__hash__() ^ RANDOM

n = II()
nums1 = LII()
nums2 = LII()

t0, t1 = nums1, []
s0, s1 = nums2, []

ans = 0

for i in range(30):
    tmp0 = [] 
    tmp1 = []
    
    mask = (1 << i) - 1
    
    new_t0, new_t1 = [], []
    for v in t0:
        if v >> i & 1: new_t1.append(v)
        else: new_t0.append(v)
    for v in t1:
        if v >> i & 1: new_t1.append(v)
        else: new_t0.append(v)
    t0, t1 = new_t0, new_t1
    
    new_s0, new_s1 = [], []
    for v in s0:
        if v >> i & 1: new_s1.append(v)
        else: new_s0.append(v)
    for v in s1:
        if v >> i & 1: new_s1.append(v)
        else: new_s0.append(v)
    s0, s1 = new_s0, new_s1
    
    cnt = 0
    pt0, pt1 = len(s0) - 1, len(s1) - 1
    for x in t0:
        x &= mask
        while pt0 >= 0 and x + (s0[pt0] & mask) > mask:
            pt0 -= 1
        cnt += len(s0) - pt0 - 1
        while pt1 >= 0 and x + (s1[pt1] & mask) > mask:
            pt1 -= 1
        cnt += pt1 + 1

    pt0, pt1 = len(s1) - 1, len(s0) - 1
    for x in t1:
        x &= mask
        while pt0 >= 0 and x + (s1[pt0] & mask) > mask:
            pt0 -= 1
        cnt += len(s1) - pt0 - 1
        while pt1 >= 0 and x + (s0[pt1] & mask) > mask:
            pt1 -= 1
        cnt += pt1 + 1
    

    if cnt & 1: ans |= 1 << i

print(ans)
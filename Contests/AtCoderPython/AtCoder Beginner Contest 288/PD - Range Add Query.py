import bisect
import collections
import itertools
import math
import os
import random
import sys
from functools import reduce
from heapq import *
from io import BytesIO, IOBase

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

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, k = map(int, input().split())
    arr = ints()

    # d = [0] * n
    # cur = 0
    # for i, a in enumerate(arr):
    #     cur += d[i]
    #     d[i] -= cur + a
    #     if i + k < n:
    #         d[i + k] += cur + a
    #     cur -= cur + a
    # print(d)

    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        
        check = True
        last = r - k
        for i in range(r - k + 1, r):
            if i - k < l - 1:
                pre = 0
            elif i - k == l - 1:
                pre = arr[i - k]
            else:
                pre = arr[i - k] - arr[i - k - 1]
            # print(pre)
            if arr[i] - arr[i - 1] + pre != 0:
                check = False
            if arr[i]: last = i

        if check:
            print("Yes")
            continue
        
        if last - l + 2 >= k:
            check = True
            for i in range(last, last - k + 1, -1):
                if arr[i] != arr[i - 1]:
                    check = False
                    break
            if check:
                print("Yes")
                continue

        print("No")
        

# t = int(input())
t = 1
for _ in range(t):
    solve()
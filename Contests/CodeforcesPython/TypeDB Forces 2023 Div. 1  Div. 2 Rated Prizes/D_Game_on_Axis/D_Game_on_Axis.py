import collections
import math
import os
import random
import sys
from bisect import bisect, bisect_left
from functools import reduce
from heapq import heapify, heappop, heappush
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
    n = int(input())
    arr = ints()

    valid = [False] * n
    check = [False] * n
    ans = n + 1 # 点1到范围外的可能数

    j = 0
    check[j] = True
    m = 1
    while 0 <= j + arr[j] < n and not check[j + arr[j]]:
        j += arr[j]
        ans += n + 1    # 点1会到此点，此点到范围外的可能数
        m += 1
        check[j] = True
    if j + arr[j] >= n or j + arr[j] < 0:
        valid[0] = valid[j] = True
    else:
        valid[0] = valid[j] = valid[j + arr[j]]
    
    if valid[0]:
        ans += (n * 2 + 1) * (n - m)    # 点1循环外的点可能数
        ans += m * (m - 1) // 2         # 提前往后面跳的可能数

    valid[0] = False

    for i in range(1, n):
        if check[i]: continue
        j = i
        check[j] = True
        k = 1
        while 0 <= j + arr[j] < n and not check[j + arr[j]]:
            j += arr[j]
            k += 1
            check[j] = True
        if j + arr[j] >= n or j + arr[j] < 0:
            valid[i] = valid[j] = True
            ans += m * k
        elif j + arr[j] != 0 and valid[j + arr[j]]:
            valid[i] = valid[j] = valid[j + arr[j]]
            ans += (m - 1) * k
        # if valid[i]: ans += m * k

    print(ans)

t = int(input())
for _ in range(t):
    solve()
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
    n, m = map(int, input().split())
    arr = []
    # pos1 = [[] for _ in range(n)]
    # pos0 = [[] for _ in range(n)]
    cnt = [0] * n
    tot = 0
    used = [[False] * m for _ in range(n)]
    for i in range(n):
        arr.append(ints())
        # for i, a in enumerate(arr[-1]):
        # for a in enumerate
        #     if a:
        #         cnt[i] += 1
                # pos[i].append(i + 1)
        # cnt[i] = len(pos[i])
        cnt[i] = sum(arr[-1])
        tot += cnt[i]

    if tot % n != 0:
        print(-1)
        return

    target = tot // n
        
    idx = sorted(list(range(n)), key = lambda x: cnt[x])

    ans = []
    l, r = 0, n - 1
    while l < r:
        if cnt[idx[l]] == target:
            l += 1
            continue
        if cnt[idx[r]] == target:
            r -= 1
            continue

        i = 0
        while i < m and cnt[idx[l]] < target and cnt[idx[r]] > target:
            if arr[idx[l]][i] == 0 and arr[idx[r]][i] == 1 and not used[idx[l]][i] and not used[idx[r]][i]:
                ans.append((idx[l] + 1, idx[r] + 1, i + 1))
                cnt[idx[l]] += 1
                cnt[idx[r]] -= 1
                used[idx[l]][i] = True
                used[idx[r]][i] = True
                
            i += 1

    print(len(ans))
    for x, y, z in ans:
        print(x, y, z)

t = int(input())
for _ in range(t):
    solve()
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
    s = input()
    cnt = collections.Counter(s)

    d = collections.Counter(cnt.values())

    l = len(d)
    if l == 1:
        print(0)
        print(s)
        return

    left = [0] * len(cnt)
    for i, v in enumerate(sorted(cnt.values())):
        if i == 0:
            left[i] = v
        else:
            left[i] = left[i - 1] + v

    ans = n
    tk = n
    pres = prev = 0
    sv = len(cnt)
    mn = (n + 25) // 26 - 1

    for k in range(n, mn, -1):
        pres += d[k] * k
        prev += d[k]
        if n % k == 0:
            targetc = n // k
            temp = pres - k * prev
            if targetc < sv:
                temp += left[sv - targetc - 1]
            if temp < ans:
                ans = temp
                tk = k

    targetc = n // tk
    rep = set()
    to1 = []
    
    c = sv - targetc
    for k, v in sorted(cnt.items(), key = lambda x: x[1]):
        if c > 0:
            rep.add(k)
        elif v < tk:
            to1.append(k)
        c -= 1
    # print(rep)

    to2 = []
    for k in range(26):
        c = chr(97+ k)
        if cnt[c] == 0:
            to2.append(c)

    rt = list(s)
    for i in range(n):
        if cnt[rt[i]] > tk or rt[i] in rep:
            cnt[rt[i]] -= 1
            if to1:
                rt[i] = to1[-1]
                cnt[to1[-1]] += 1
                if cnt[to1[-1]] == tk:
                    to1.pop()
            elif to2:
                rt[i] = to2[-1]
                cnt[to2[-1]] += 1
                if cnt[to2[-1]] == tk:
                    to2.pop()

    print(ans)
    print("".join(rt))

t = int(input())
for _ in range(t):
    solve()
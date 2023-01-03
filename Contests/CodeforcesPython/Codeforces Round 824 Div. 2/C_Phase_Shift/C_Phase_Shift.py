import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

# Sample Inputs/Output 
# region fastio
import sys, os
from io import BytesIO, IOBase
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

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n = int(input())
    s = input()
    d = dict()
    sd = dict()
    ans = [""] * n
    cur = 0
    cnt = 0
    fa = list(range(26))
    def find(x):
        cur = x
        while x != fa[x]:
            x = fa[x]
        if cur != x:
            fa[cur], cur = x, fa[x]
        return x
    for i, c in enumerate(s):
        if c not in d:
            # while chr(cur+97) == c or (chr(cur+97) in d and cur <= 25):
            cur = 0
            while chr(cur+97) == c or (chr(cur + 97) in sd and sd[chr(cur + 97)] != c) or (cnt < 25 and find(cur) == find(ord(c) - 97)):
                cur = (cur + 1) % 26
            d[c] = chr(cur+97)
            sd[chr(cur + 97)] = c
            fa[cur] = ord(c) - 97
            cnt += 1
            cur = (cur + 1) % 26
        # elif

        ans[i] = d[c]
    
    print("".join(ans))

t = int(input())
for _ in range(t):
    solve()
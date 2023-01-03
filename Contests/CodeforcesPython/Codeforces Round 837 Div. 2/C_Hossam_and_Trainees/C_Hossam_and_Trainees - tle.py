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

# MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

mxn = 10 ** 5 + 5
isprime = [True] * (mxn + 1)
primes = list()
def init():
    isprime[0] = isprime[1] = False
    for i in range(4, mxn, 2):
        isprime[i] = False
    i = 3
    while i < mxn // i:
        if not isprime[i]: 
            i += 2
            continue
        for j in range(i * i, mxn, i + i):
            isprime[j] = False
        i += 2
    
    for i in range(2, mxn):
        if isprime[i]:
            primes.append(i)

exist = [0] * mxn
vid = 0
st = set()

def solve() -> None:
    n = int(input())
    arr = ints()

    ans = False

    def check(x):
        nonlocal ans
        if exist[x] == vid:
            ans = True
            return
        exist[x] = vid
    
    for a in arr:
        if a < mxn and isprime[a]:
            check(a)
            if ans:
                break
            continue

        for p in primes:
            if a == 1 or p * p >=a:
                break
            if a % p == 0:
                check(p)
                if ans:
                    break
                while a % p == 0:
                    a //= p
        if a > 1:
            if a < mxn:
                check(a)
                continue
            if a in st:
                ans = True
                break
            st.add(a)

    print("YES" if ans else "NO")

init()
t = int(input())
for _ in range(t):
    vid += 1
    st.clear()
    solve()
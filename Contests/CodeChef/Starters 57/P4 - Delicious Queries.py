from bisect import bisect, bisect_left
from itertools import accumulate
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

C = 10 ** 5
isprime = [True] * (C + 1)
prime = [[] for _ in range(C + 1)]  # prime factors of all number, e.g., 4: 2, 10: 2, 5, 20: 2, 5

def calPrime() -> None:
    # 埃拉托斯特尼筛法
    for i in range(2, C + 1):
        if isprime[i]:
            for j in range(i, C + 1, i):
                isprime[j] = False
                prime[j].append(i)

def solve() -> None:
    n = int(input())
    arr = ints()

    presum = list(accumulate(arr))
    
    factors = [[] for _ in range(C + 1)]
    for i, a in enumerate(arr):
        for p in prime[a]:
            factors[p].append(i)    # Put Mi into its prime factors, e.g., Mi = 10, 2: 10, 5: 10
            
    pf = [[] for _ in range(C + 1)]
    sf = [[] for _ in range(C + 1)]

    for i in range(C + 1):
        if not factors[i]:
            continue
        
        tmp = [0] * len(factors[i])
        for j in range(len(factors[i])):
            tmp[j] = arr[factors[i][j]]

        pf[i] = list(accumulate(tmp))
        tmp.sort(reverse=True)
        sf[i] = list(accumulate(tmp))

    q = int(input())
    for _ in range(q):
        p, k = map(int, input().split())
        ans = presum[k-1]

        cnt = bisect(factors[p], k) - 1
        ans += sf[p][cnt-1] - pf[p][cnt]

        print(ans)

calPrime()
t = int(input())
for _ in range(t):
    solve()

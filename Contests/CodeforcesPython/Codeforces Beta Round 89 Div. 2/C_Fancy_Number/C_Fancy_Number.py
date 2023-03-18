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
    s = list(input())

    cnt = Counter(s)
    if cnt.most_common(1)[0][1] >= k:
        print(0)
        print("".join(s))
        return

    right = [Counter() for _ in range(10)]
    left = [Counter() for _ in range(10)]
        
    def f(x: str) -> int:
        d = k - cnt[x]
        x = int(x)

        l, r = x - 1, x + 1
        res = 0
        while d:
            if r <= 9:
                mn = min(cnt[str(r)], d)
                if mn:
                    res += mn * (r - x)
                    d -= mn
                    right[x][str(r)] = mn
                r += 1
            if l >= 0:
                mn = min(cnt[str(l)], d)
                if mn:
                    res += mn * (x - l)
                    d -= mn
                    left[x][str(l)] = mn
                l -= 1
        return res

    def f2(x: str) -> str:
        res = s.copy()
        d = k - cnt[x]
        xi = int(x)

        for i in range(n):
            if right[xi][res[i]]:
                right[xi][res[i]] -= 1
                res[i] = x
                d -= 1
                if d == 0:
                    break
        if d == 0:
            return "".join(res)

        for i in range(n - 1, -1, -1):
            if left[xi][res[i]]:
                left[xi][res[i]] -= 1
                res[i] = x
                d -= 1
                if d == 0:
                    break

        return "".join(res)

        # l, r = int(x) - 1, int(x) + 1
        # while d:
        #     if r <= 9:
        #         rs = str(r)
        #         mn = min(cnt[rs], d)
        #         d -= mn
        #         i = 0
        #         while mn:
        #             if res[i] == rs:
        #                 res[i] = x
        #                 mn -= 1
        #             i += 1
        #         r += 1
        #     if l >= 0:
        #         ls = str(l)
        #         mn = min(cnt[ls], d)
        #         d -= mn
        #         i = n - 1
        #         while mn:
        #             if res[i] == ls:
        #                 res[i] = x
        #                 mn -= 1
        #             i -= 1
        #         l -= 1
        # return "".join(res)

    h = []
    for x in digits:
        m = f(x)
        h.append((m, x))

    h.sort()
    m = h[0][0]
    ans = ""

    for o, x in h:
        if o > m: break
        res = f2(x)
        if not ans or res < ans: ans = res

    print(m)
    print(ans)

# for _ in range(int(input())):
solve()
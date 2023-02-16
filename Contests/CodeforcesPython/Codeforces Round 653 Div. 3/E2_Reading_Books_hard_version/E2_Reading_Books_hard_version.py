import collections
import math
import os
import random
import sys
from bisect import bisect, bisect_left
from functools import reduce
from heapq import heapify, heappop, heappush, heapreplace
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
    n, m, k = map(int, input().split())
    books = [[] for _ in range(4)]
    for i in range(1, n + 1):
        t, al, bl = map(int, input().split())
        if al and bl:
            books[0].append((t, i))
        elif al:
            books[1].append((t, i))
        elif bl:
            books[2].append((t, i))
        else:
            books[3].append((t, i))

    l = [0] * 4
    for i, book in enumerate(books):
        l[i] = len(book)

    lab = min(l[1], l[2])

    if l[0] + lab < k:
        print(-1)
        return
    
    for book in books:
        book.sort()

    ans = i = j = 0
    while i + j < k:
        if i < l[0] and j < lab and books[0][i][0] <= books[1][j][0] + books[2][j][0]:
            ans += books[0][i][0]
            i += 1
        elif i < l[0] and j < lab and books[0][i][0] > books[1][j][0] + books[2][j][0]:
            ans += books[1][j][0] + books[2][j][0]
            j += 1
        elif i < l[0]:
            ans += books[0][i][0]
            i += 1
        elif j < lab:
            ans += books[1][j][0] + books[2][j][0]
            j += 1

    idx = [0] * 4
    idx[0] = i
    idx[1] = idx[2] = j
    if sum(idx) < m:
        while sum(idx) < m and any(idx[i] < l[i] for i in range(4)):
            mn = math.inf
            o = -1
            for i in range(4):
                if idx[i] < l[i] and books[i][idx[i]][0] < mn:
                    mn = books[i][idx[i]][0]
                    o = i

            if idx[1] < l[1] and idx[2] < l[2] and idx[0] and (books[1][idx[1]][0] + books[2][idx[2]][0] - books[0][idx[0] - 1][0]) < mn:
                ans += books[1][idx[1]][0] + books[2][idx[2]][0] - books[0][idx[0] - 1][0]
                idx[1] += 1
                idx[2] += 1
                idx[0] -= 1
            else:
                ans += mn
                idx[o] += 1
        
        if sum(idx) < m:
            print(-1)
            return

    elif sum(idx) > m:
        while sum(idx) > m and idx[0] < l[0] and idx[1] and idx[2]:
            ans += books[0][idx[0]][0]
            idx[0] += 1
            idx[1] -= 1
            idx[2] -= 1
            ans -= books[1][idx[1]][0]
            ans -= books[2][idx[2]][0]
            
        if sum(idx) > m:
            print(-1)
            return
            
    pos = []
    # add positions
    for i in range(4):
        for j in range(idx[i]):
            pos.append(books[i][j][1])

    # output
    print(ans)
    print(*pos)

# t = int(input())
# for _ in range(t):
solve()
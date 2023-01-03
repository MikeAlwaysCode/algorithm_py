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

mx = 51
cnt = [[0] * 5 for _ in range(mx)]

def init():
    # cnt[i][0] : S1, cnt[i][1]: S2
    # cnt[i][2]: S1S2
    # cnt[i][3]: S2S1, cnt[i][4]: S2S2
    cnt[1][0] = cnt[2][1] = cnt[3][0] = cnt[3][1] = cnt[3][2] = 1
    for i in range(4, mx):
        pre = 1 if (i - 1) & 1 else 2
        cnt[i][0] = cnt[i-2][0] + cnt[i-1][0]
        cnt[i][1] = cnt[i-2][1] + cnt[i-1][1]
        cnt[i][2] = cnt[i-2][2] + cnt[i-1][2]
        cnt[i][3] = cnt[i-2][3] + cnt[i-1][3] + int(pre == 1)
        cnt[i][4] = cnt[i-2][4] + cnt[i-1][4] + int(pre == 2)

def solve() -> None:
    k, x, n, m = map(int, input().split())

    # print(cnt[k])

    for i in range(n // 2 + 1): # i AC in S1
        for j in range(m // 2 + 1): # j AC in S2
            if i * cnt[k][0] + j * cnt[k][1] == x:
                s1 = "AC" * i + "C" * (n - 2 * i)
                s2 = "AC" * j + "C" * (n - 2 * j)
                print(s1)
                print(s2)
                return
            elif i * cnt[k][0] + j * cnt[k][1] < x:
                l = x - i * cnt[k][0] - j * cnt[k][1]
                s1 = "AC" * i
                s2 = "AC" * j

                # cnt[i][2]: S1S2
                # cnt[i][3]: S2S1, cnt[i][4]: S2S2
                for c in range(1, 8):
                    curr = 0
                    cc = c
                    if c == 3: cc = 7
                    for b in range(3):
                        if (cc >> b) & 1:
                            curr += cnt[k][b + 2]
                    
                    if curr != l: continue

                    s1p = s1s = s2p = s2s = ""

                    if c & 1:   # S1S2
                        s1s = "A"
                        s2p = "C"

                    if (c >> 1) & 1: # S2S1
                        s1p = "C"
                        s2s = "A"

                    if (c >> 2) & 1: # S2S2
                        s2p = "C"
                        s2s = "A"
                        
                    if 2 * i + len(s1p) + len(s1s) > n or 2 * j + len(s2p) + len(s2s) > m: continue

                    cs1 = s1p + s1 + "Z" * (n - 2 * i - len(s1p) - len(s1s)) + s1s
                    cs2 = s2p + s2 + "Z" * (m - 2 * j - len(s2p) - len(s2s)) + s2s

                    print(cs1)
                    print(cs2)
                    return

            else:   # more j AC not achiveved
                break

    print("Happy new year!")

init()
# t = int(input())
t = 1
for _ in range(t):
    solve()
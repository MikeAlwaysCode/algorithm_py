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

MOD = 998244353
# MOD = 10 ** 9 + 7
# DIR = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve() -> None:
    n, m = map(int, input().split())

    def f(x, y) -> int:
        # 1. 先计算奇数行
        #   1.1 第一行第1个元素是1，第一行的元素个数是(y + 1) // 2, 最后一个元素是y - 1 + (y & 1)
        #   1.2 第一行元素和为：(1 + y - 1 + (y & 1)) * (y + 1) // 4 = (y + (y & 1)) * (y + 1) // 4
        #   1.3 总奇数行数为：(x + 1) // 2
        #   1.4 奇数行之间的差为奇数行元素个数*2m，即：2m * ((y + 1) // 2)
        #   1.5 最后一个奇数行的元素和为：
        #       (y + (y & 1)) * (y + 1) // 4 + m * (y + 1) * ((x + 1) // 2 - 1)
        #     = (y + (y & 1)) * (y + 1) // 4 + m * (y + 1) * (x - 1) // 2
        #   1.6 奇数行之和为:
        #       ((y + (y & 1)) * (y + 1) // 4 + (y + (y & 1)) * (y + 1) // 4 + 2m * ((y + 1) // 2) * (x - 1) // 2) * (x + 1) // 4
        #     = ((y + (y & 1)) * (y + 1) // 2 + 2m * ((y + 1) // 2) * (x - 1) // 2) * (x + 1) // 4
        #     = ((y + 1) // 2) * ((x + 1) // 2) * (y + (y & 1) + 2m * (x - 1) // 2)
        sodd = ((y + 1) // 2) * ((x + 1) // 2) * (y + (y & 1) + 2 * m * ((x - 1) // 2)) // 2

        # 2. 再计算偶数行
        # 2.1 第二行第1个元素是m + 2, 第二行的元素个数是y // 2, 最后一个元素是m + y - (y & 1)
        # 2.2 第二行的元素和为：(m + 2 + m + y - (y & 1)) * y // 4 = (2m + 2 + y - (y & 1)) * y // 4
        # 2.3 总偶数行数为：x // 2
        # 2.4 偶数行之间的差为偶数行元素个数*2m，即：2m * y // 2
        # 2.5 最后一个偶数行的元素和为：
        #     ((2m + 2 + y - (y & 1)) * y // 4 + m * y * (x // 2 - 1))
        # 2.6 偶数行之和为：
        #     ((2m + 2 + y - (y & 1)) * y // 4 + ((2m + 2 + y - (y & 1)) * y // 4 + 2m * y // 2 * (x // 2 - 1))) * x // 4
        #   = ((2m + 2 + y - (y & 1)) * y // 2 + 2m * y // 2 * (x // 2 - 1))) * x // 4
        #   = (2 + y - (y & 1) + 2m * (x // 2)) // 2 * (y // 2) * (x // 2)
        seven = (2 + y - (y & 1) + 2 * m * (x // 2)) // 2 * (y // 2) * (x // 2)
        # seven = ((2 + y - (y & 1)) + m * x) % MOD * y % MOD * x % MOD * pow(8, MOD - 2, MOD) % MOD
        # print(x, y, "odd:", sodd, "even:", seven)
        return sodd + seven
        '''
        s1 = (2 + (y - 1) // 2 * 2) * ((y + 1) //2) // 2
        s2 = (2 * m + 4 + (y // 2 - 1) * 2) * (y // 2) // 2
        
        if x & 1:
            xo = x
        else:
            xo = x - 1
        so = ((2*xo - 2) * m + 2 + (y - 1) // 2 * 2) * ((y + 1) //2) // 2
        totOdd = (s1 + so) * ((xo + 1) // 2) // 2
        
        if x & 1:
            xe = x - 1
        else:
            xe = x
        se = ((2*xe - 2) * m + 4 + (y // 2 - 1) * 2) * (y // 2) // 2
        totEven = (s2 + se) * (xe // 2) // 2

        return (totOdd + totEven) % MOD
        '''

    q = int(input())
    for _ in range(q):
        a, b, c, d = map(int, input().split())
        print((f(b, d) - f(a - 1, d) - f(b, c - 1) + f(a - 1, c - 1)) % MOD)

# t = int(input())
t = 1
for _ in range(t):
    solve()
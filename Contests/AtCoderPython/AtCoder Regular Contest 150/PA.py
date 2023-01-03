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
    n, k = map(int, input().split())
    s = input()
    cnt0 = [0] * (n + 1)
    cnt1 = [0] * (n + 1)
    for i in range(n):
        cnt0[i+1] = cnt0[i] + (s[i] == "0")
        cnt1[i+1] = cnt1[i] + (s[i] == "1")
    
    cnt = 0
    for i in range(k, n+1):
        if cnt0[i] == cnt0[i-k] and cnt1[i] == cnt1[n] and not cnt1[i-k]:
            cnt += 1

    if cnt != 1:
        print("No")
    else:
        print("Yes")

    '''
    s = input() + "0"
    m = s.count("1")
    if m > k:
        print("No")
        return

    l, cnt, o = -1, 0, 0
    l1 = r1 = -1
    for i, c in enumerate(s):
        if c != "0":
            if l == -1:
                l = i
            if c == "1":
                o += 1
                if l1 == -1:
                    l1 = i
                r1 = i
        elif l != -1:
            # print(o, l, i)
            if 0 < o < m:
                # print(1)
                print("No")
                return
            
            if m > 0 and o == 0:
                l = l1 = -1
                o = 0
                continue

            if (i - l) == k:
                if o == m:
                    cnt += 1
            elif (i - l) > k:
                if m == 0:
                    print("No")
                    return
                    # cnt += 1
                    # l = l1 = -1
                    # o = 0
                    # continue
                
                if r1 - l1 + 1 > k:
                    # print(2)
                    print("No")
                    return
                elif r1 - l1 + 1 == k:
                    cnt += 1
                elif s[l] == "1" or s[i-1] == "1":
                    cnt += 1
                else:
                    # print(3)
                    print("No")
                    return

            if cnt > 1:
                print("No")
                return

            l = l1 = -1
            o = 0
    # print(cnt)
    if cnt != 1:
        print("No")
    else:
        print("Yes")
    '''

t = int(input())
for _ in range(t):
    solve()
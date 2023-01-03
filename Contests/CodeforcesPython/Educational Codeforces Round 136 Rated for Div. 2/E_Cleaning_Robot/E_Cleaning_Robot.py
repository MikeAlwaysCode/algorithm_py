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
    s = []
    s.append(list(map(int, list(input()))) + [0])
    s.append(list(map(int, list(input()))) + [0])
    
    dp = [[-math.inf] * 2 for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(2):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + s[j][i+1])
            if s[j^1][i]:
                if i < n - 1:
                    dp[i+2][j^1] = max(dp[i+2][j^1], dp[i][j] + 1 + s[j^1][i+1] + s[j^1][i+2])
                else:
                    dp[i+1][j^1] = max(dp[i+1][j^1], dp[i][j] + 1 + s[j^1][i+1])

    print(max(dp[n]))
    '''
    n=inpint()
    s=[]
    for i in range(2):
        s.append([i for i in list(input())]+['0','0'])
    #print(arr)
    f=[[-inf]*(2) for _ in range(n+2)]
    f[0][0]=0
    for i in range(n):
        for j in range(2):
            f[i+1][j]=max(f[i+1][j],f[i][j]+int(s[j][i+1]))
            if s[j^1][i]=='1':
                f[min(i+2,n)][j^1]=max(f[min(i+2,n)][j^1],f[i][j]+1+int(s[j^1][i+1])+int(s[j^1][i+2]))
    print(max(f[n][0],f[n][1]))
    '''
    '''
    N = int(input())
    G = [[int(x) for x in input()] + [0] for _ in range(2)]
    
    dp = [[0] * 2  for _ in range(N + 1)]   # number of 1 cells robot will clean when it arrives at cell (j, i) from the left
    for j in range(2):
        dp[N - 1][j] = G[1 - j][N - 1]
    
    for i in range(N - 2, - 1, -1):
        for j in range(2):
            dp[i][j] = G[j][i + 1] + dp[i + 1][j]   # base case: ignore row 1 - j and proceed right
            if G[1 - j][i]:
                dp[i][j] = max(dp[i][j], 1 + G[1 - j][i + 1] + G[1 - j][i + 2] + dp[i + 2][1 - j])
 
    print(dp[0][0])
    '''

t = 1
for _ in range(t):
    solve()
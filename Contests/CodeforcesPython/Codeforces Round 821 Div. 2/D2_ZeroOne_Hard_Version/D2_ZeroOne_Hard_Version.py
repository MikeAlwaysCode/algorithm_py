import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n, x, y = map(int, input().split())
    A = list(map(int, list(input().strip())))
    B = list(map(int, list(input().strip())))

    d = 0
    for i in range(n):
        A[i] ^= B[i]
        d += A[i]
    
    if d & 1:
        print(-1)
        return
    elif d == 2:
        l, r = 0, n - 1
        while not A[l]:
            l += 1
        while not A[r]:
            r -= 1
        if l + 1 == r:
            print(min(x, y * 2))
        else:
            print(min((r - l) * x, y))
        return
    elif d == 0 or x >= y:
        print(d // 2 * y)
        return
    
    z0 = [[1<<60] * (n + 1) for _ in range(n)]
    z1 = [[1<<60] * (n + 1) for _ in range(n)]

    if A[0]:
        z1[0][1] = 0
    else:
        z0[0][0] = 0
    
    for i in range(1, n):
        if A[i]:
            for j in range(i + 1, -1, -1):
                if j <= i:
                    z0[i][j] = min(z0[i - 1][j + 1] + y, z1[i - 1][j + 1] + x)
                if j:
                    z0[i][j] = min({z0[i][j], z0[i - 1][j - 1] + x, z1[i - 1][j - 1] + y})
                    z1[i][j] = min(z0[i - 1][j - 1], z1[i - 1][j - 1])
        else:
            for j in range(i + 1, -1, -1):
                z0[i][j] = min(z0[i - 1][j], z1[i - 1][j])
                z1[i][j] = min(z0[i - 1][j] + y, z1[i - 1][j] + x)
                if j > 1:
                    z1[i][j] = min({z1[i][j], z0[i - 1][j - 2] + x, z1[i - 1][j - 2] + y})

    print(z0[n-1][0])
    
t = int(input())
for _ in range(t):
    solve()
import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

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
    else:
        print(d // 2 * y)
    
    

t = int(input())
for _ in range(t):
    solve()
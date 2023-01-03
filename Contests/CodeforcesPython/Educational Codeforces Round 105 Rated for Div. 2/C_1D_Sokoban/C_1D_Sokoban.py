from bisect import bisect
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

def cal(a: list[int], b: list[int]) -> int:
    if not a or not b:
        return 0
    
    na, nb = len(a), len(b)
    inplace = 0
    i = j = 0
    while i < na and j < nb:
        if a[i] == b[j]:
            inplace += 1
            i += 1
            j += 1
        elif abs(a[i]) > abs(b[j]):
            j += 1
        else:
            i += 1

    i = k = 0
    ans = inplace
    for j in range(nb):
        while i < na and abs(a[i]) < abs(b[j]):
            i += 1

        if i < na and a[i] == b[j]:
            inplace -= 1
            i += 1
        
        while k < nb and abs(b[k]) <= abs(b[j]) - i:
            k += 1
        # print(j, k)
        ans = max(ans, j - k + 1 + inplace)

    return ans
    

def solve() -> None:
    n, m = map(int, input().split())
    A = ints()
    B = ints()

    idx = bisect(A, 0)
    a1 = A[:idx][::-1]
    a2 = A[idx:]
    idx = bisect(B, 0)
    b1 = B[:idx][::-1]
    b2 = B[idx:]

    print(cal(a1, b1) + cal(a2, b2))

t = int(input())
for _ in range(t):
    solve()
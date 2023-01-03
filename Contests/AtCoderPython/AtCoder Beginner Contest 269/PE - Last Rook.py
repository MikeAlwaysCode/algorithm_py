import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def printQry(a, b, c, d) -> None:
    sa = str(a)
    sb = str(b)
    sc = str(c)
    sd = str(d)
    print(f"? {sa} {sb} {sc} {sd}", flush = True)

def printAns(ans1, ans2) -> None:
    s1 = str(ans1)
    s2 = str(ans2)
    print(f"! {s1} {s2}", flush = True)

def solve() -> None:
    n = int(input())
    
    l, r = 1, n
    while l <= r:
        b = (r + l) // 2
        printQry(l, b, 1, n)
        ans = int(input())
        if ans == b - l + 1:
            l = b + 1
        else:
            r = b - 1
    res1 = l
    l, r = 1, n
    while l <= r:
        b = (r + l) // 2
        printQry(1, n, l, b)
        ans = int(input())
        if ans == b - l + 1:
            l = b + 1
        else:
            r = b - 1
    res2 = l
    printAns(res1, res2)

# t = int(input())
# for _ in range(t):
solve()
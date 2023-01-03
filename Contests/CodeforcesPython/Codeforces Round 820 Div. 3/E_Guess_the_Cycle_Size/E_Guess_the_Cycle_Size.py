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
    for q in range(2, 27):
        printQry(1, q)
        d1 = int(input())

        if d1 == -1:
            printAns(q - 1)
            return

        printQry(q, 1)
        d2 = int(input())

        if d1 != d2:
            printAns(d1 + d2)
            return

# t = int(input())
# for _ in range(t):
solve()
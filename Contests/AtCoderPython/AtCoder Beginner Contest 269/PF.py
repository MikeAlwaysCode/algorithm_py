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
    MOD = 998244353
    n, m = map(int, input().split())

    def cal(x, y) -> int:
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

    q = int(input())
    for _ in range(q):
        a, b, c, d = map(int, input().split())
        print((cal(b, d) - cal(a - 1, d) - cal(b, c - 1) + cal(a - 1, c - 1)) % MOD)

# t = int(input())
# for _ in range(t):
solve()
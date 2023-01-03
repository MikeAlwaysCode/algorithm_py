import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n, m, k = map(int, input().split())

    tot = n * m
    
    if k > tot:
        print("NO")
        return
    
    if k == tot:
        print("YES")
        return
    
    l = tot - k
    # mxr = n - l // m
    # print(mxr)
    # for r in range(mxr + 1):
    for r in range(n):
        if (n - r) * m < l:
            break
        if l % (n - r) == 0:
            # print(r)
            print("YES")
            return
    
    print("NO")


t = int(input())
for _ in range(t):
    solve()
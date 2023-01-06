import collections
import math
import random
import sys
from functools import *
from heapq import *

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    
    def findprime(x: int) -> int:
        for d in range(2, x + 1):
            if d * d > x: break
            if x % d == 0: return d
        return -1
    
    p = findprime(n)
    if n == 1 or p == -1 or p * p == n: print(-1)
    else: print(1, p, n // p)

t = int(input())
for _ in range(t):
    solve()
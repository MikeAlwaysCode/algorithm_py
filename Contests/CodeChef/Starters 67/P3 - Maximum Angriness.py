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
    n, k = map(int, input().split())

    if n == 1:
        print(0)
        return
    
    if k >= n // 2:
        print(n * (n - 1) // 2)
    else:
        print((2 * n - k - 1) * k // 2 + (n - 2 * k) * k + k * (k - 1) // 2)

t = int(input())
for _ in range(t):
    solve()
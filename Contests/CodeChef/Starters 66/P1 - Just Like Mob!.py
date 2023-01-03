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
    n, m, k, x = map(int, input().split())
    
    d = n * k + m

    left = x % d

    print("YES" if left == 0 or left > n * (k - 1) else "NO")

t = int(input())
for _ in range(t):
    solve()
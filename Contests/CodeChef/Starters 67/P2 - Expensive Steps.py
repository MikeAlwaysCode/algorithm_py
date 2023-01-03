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
    n, x1, y1, x2, y2 = map(int, input().split())
    
    print(min(min(x1, y1, n - x1 + 1, n - y1 + 1) + min(x2, y2, n - x2 + 1, n - y2 + 1), abs(x1 - x2) + abs(y1 - y2)))

t = int(input())
for _ in range(t):
    solve()
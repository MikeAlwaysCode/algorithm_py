import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    
    if n & 1:
        ans = [1, 2, 3] + list(range(n-2, 3, -1)) + [n-1, n]
    else:
        ans = list(range(n-2, 0, -1)) + [n-1, n]

    print(*ans)

t = int(input())
for _ in range(t):
    solve()
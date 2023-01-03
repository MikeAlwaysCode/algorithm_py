import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    ans = 0
    for _ in range(n):
        ans += int(input())
        print(ans)

# t = int(input())
# for _ in range(t):
solve()
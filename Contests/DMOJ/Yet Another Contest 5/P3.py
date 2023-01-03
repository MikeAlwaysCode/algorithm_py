import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    
    ans = list(range(n, 0, -1))
    if n == 3:
        ans.append(3)
    elif n > 3:
        ans.append(3)

    print(*ans)

# t = int(input())
# for _ in range(t):
solve()
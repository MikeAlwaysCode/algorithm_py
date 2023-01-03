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
    l = [0] * n
    r = [0] * n
    for i in range(n):
        l[i], r[i] = map(int, input().split())
        
    l.sort(reverse=True)
    r.sort()

    ans = 0
    for i in range(n):
        ans += max(0, l[i] - r[i]) * (n - 2 * i - 1)

    print(ans)

# t = int(input())
# for _ in range(t):
solve()
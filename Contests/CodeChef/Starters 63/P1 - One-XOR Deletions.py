import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    arr = ints()
    
    d = collections.defaultdict(int)
    for a in arr:
        d[a ^ (a & 1)] += 1
    
    print(n - max(d.values()))

t = int(input())
for _ in range(t):
    solve()
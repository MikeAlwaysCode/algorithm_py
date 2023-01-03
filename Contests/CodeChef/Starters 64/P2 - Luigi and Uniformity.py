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
    
    g = 0
    for a in arr:
        g = math.gcd(g, a)

    ans = 0
    for a in arr:
        if a > g:
            ans += 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()
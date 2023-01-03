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
    n, x, c = map(int, input().split())
    arr = ints()

    print(sum(max(a, x - c) for a in arr))
    
    # ans = 0
    # for a in arr:
    #     if x - a > c:
    #         ans += x - c
    #     else:
    #         ans += a
    # print(ans)

t = int(input())
for _ in range(t):
    solve()
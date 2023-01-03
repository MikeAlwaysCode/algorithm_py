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
    # x = k + n % k
    x = k
    while 0 < n % x < k:
        x += 1
    ans = list(i%x+1 for i in range(n))

    print(x)
    print(*ans)

t = int(input())
for _ in range(t):
    solve()
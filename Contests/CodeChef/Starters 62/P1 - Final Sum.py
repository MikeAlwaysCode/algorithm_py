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
    n, q = map(int, input().split())
    arr = ints()
    ans = sum(arr)
    for _ in range(q):
        l, r = map(int, input().split())
        if not (r - l) & 1:
            ans += 1

    print(ans)

t = int(input())
for _ in range(t):
    solve()
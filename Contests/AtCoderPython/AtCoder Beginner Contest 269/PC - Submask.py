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
    k = bin(n)[2:].count("1")
    pos = []
    cur = 0
    while n:
        if n & 1:
            pos.append(cur)
        cur += 1
        n >>= 1
    # print(pos)

    for i in range(pow(2, k)):
        ans = 0
        cur = 0
        while i:
            if i & 1:
                ans += (1 << pos[cur])
            cur += 1
            i >>= 1
        print(ans)

# t = int(input())
# for _ in range(t):
solve()
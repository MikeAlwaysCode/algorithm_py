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
    arr = ints()

    c = collections.Counter(arr)
    k = c.most_common(1)[0][1]
    print(math.ceil(math.log2(k)))

t = int(input())
for _ in range(t):
    solve()
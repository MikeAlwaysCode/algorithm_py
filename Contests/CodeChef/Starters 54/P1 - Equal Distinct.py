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

    cnt = collections.Counter(arr)

    c = sum(v == 1 for v in cnt.values())

    if not c & 1 or len(cnt) > c:
        print("Yes")
    else:
        print("No")

t = int(input())
for _ in range(t):
    solve()
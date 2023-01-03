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
    arr = list(map(int, input().split()))

    cnt = [0] * n
    for i, a in enumerate(arr):
        k = (i - a) % n
        # print(k)
        cnt[k-1] += 1
        cnt[k] += 1
        cnt[(k+1)%n] += 1

    print(max(cnt))

# t = int(input())
# for _ in range(t):
solve()
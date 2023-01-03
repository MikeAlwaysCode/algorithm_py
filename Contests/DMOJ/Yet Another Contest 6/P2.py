import collections
import itertools
import math
import random
import sys
from functools import reduce
from heapq import heapify, heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    s = ints()
    t = ints()

    cnt = 0
    for i in range(n):
        if (s[i] == -1 or t[i] == -1) and (s[i] != t[i]):
            print(-1)
            return
        if s[i] != t[i]:
            cnt += 1

    print(cnt)

# t = int(input())
# for _ in range(t):
solve()
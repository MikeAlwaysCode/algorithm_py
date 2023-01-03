import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    s = input().strip()
    t = input().strip()

    if len(s) > len(t):
        print("No")
    else:
        if s == t[:len(s)]:
            print("Yes")
        else:
            print("No")

# t = int(input())
# for _ in range(t):
solve()
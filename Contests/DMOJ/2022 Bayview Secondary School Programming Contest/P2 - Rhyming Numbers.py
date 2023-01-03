import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    a, b = map(int, input().split())
    if (a % 10 == 7 and a % 100 != 17 and b % 100 == 11) or (b % 10 == 7 and b % 100 != 17 and a % 100 == 11):
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()
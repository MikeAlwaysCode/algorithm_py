import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    s = input()
    
    ans = s.find("1", 1)
    if ans == -1:
        print(n)
    else:
        print(ans)

t = int(input())
for _ in range(t):
    solve()
import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    a, b = map(int, input().split())
    
    while a != b:
        mx = max(a, b)
        mn = min(a, b)
        if mx % mn != 0:
            print("NO")
            return
        
        a, b = mn, mx // mn
    print("YES")

t = int(input())
for _ in range(t):
    solve()
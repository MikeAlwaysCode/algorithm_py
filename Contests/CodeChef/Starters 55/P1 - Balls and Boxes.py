import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    x, y = map(int, input().split())

    z = 2 * x - y

    if z < x:
        x, z = z, x
    
    if z < y:
        x -= y - z
        z = y
    
    if x > y:
        z += x - y
        x = y

    print(x, y, z)

t = int(input())
for _ in range(t):
    solve()
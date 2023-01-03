import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    a = c = d = 0
    b = 10
    for i in range(10):
        s = input().strip()
        j =  s.find("#") 
        if j != -1 and a == 0:
            a = i + 1
            c = j + 1
            d = s.rfind("#") + 1
        elif j == -1 and a > 0 and b > i:
            b = i
    
    print(a, b)
    print(c, d)

# t = int(input())
# for _ in range(t):
solve()
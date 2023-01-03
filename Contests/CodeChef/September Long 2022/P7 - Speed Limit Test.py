import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    A, B, X, Y = map(int, input().split())
    
    a, b = A * Y, B * X

    print("Alice") if a > b else print("Bob") if a < b else print("Equal")


t = int(input())
for _ in range(t):
    solve()
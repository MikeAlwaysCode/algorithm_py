import collections
import math
import random
import sys
from functools import *
from heapq import *

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    x, y = map(int, input().split())
    
    print("YES" if x > y * 10 else "NO")

t = int(input())
for _ in range(t):
    solve()
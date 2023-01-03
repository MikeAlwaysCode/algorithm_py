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
    arr = ints()
    
    print("YES" if sum(arr) == max(arr) * 2 else "NO")

t = int(input())
for _ in range(t):
    solve()
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
    
    if x == y:
        print(x)
        return
        
    n = x * y // math.gcd(x, y)
    n = (n - x - y) % n
    print(n)

t = int(input())
for _ in range(t):
    solve()
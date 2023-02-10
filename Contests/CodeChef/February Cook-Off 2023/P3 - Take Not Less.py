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

    n = int(input())
    arr = ints()
    cnt = collections.Counter(arr)
    for v in sorted(cnt.values(), reverse = True):
        if v & 1:
            print("Marichka")
            return
    
    print("Zenyk")

    
t = int(input())
for _ in range(t):
    solve()
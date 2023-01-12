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

    for bit in range(20):
        xor0 = xor1 = 0
        for a in arr:
            c = (a >> bit) & 1
            if c ^ xor1:
                xor1 = 0
            else:
                xor1 = 1
            if c ^ xor0:
                xor0 = 1
            else:
                xor0 = 0
        if xor0 and xor1:
            print("NO")
            return
    print("YES")

t = int(input())
for _ in range(t):
    solve()
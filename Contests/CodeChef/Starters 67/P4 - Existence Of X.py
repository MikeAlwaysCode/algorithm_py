import collections
import math
import random
import sys
from functools import reduce
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    A, B, C = map(int, input().split())
    
    carry = 0 # to 必须进1
    for bit in range(28):
        a, b, c = A >> bit & 1, B >> bit & 1, C >> bit & 1
        if a == b:
            if carry:
                cur = c ^ 1
            else:
                cur = c
            carry = cur ^ a
    if carry:
        print("No")
    else:
        print("Yes")

t = int(input())
for _ in range(t):
    solve()
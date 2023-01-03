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
    A = ints()
    B = ints()

    ans = curr = 0
    for i in range(n):
        if A[i] and B[i]:
            curr += 1
            ans = max(ans, curr)
        else:
            curr = 0
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()
import itertools
import math
import os
import random
import sys
from bisect import bisect, bisect_left
from collections import *
from functools import reduce
from heapq import heapify, heappop, heappush
from io import BytesIO, IOBase
from string import *

# region fastio
input = lambda: sys.stdin.readline().strip()
ints = lambda: list(map(int, input().split()))
# endregion fastio

def solve() -> None:
    n, k = map(int, input().split())
    A = ints()
    W = ints()

    A.sort()
    W.sort(reverse = True)
    ans, i, j = 0, 0, n - 1

    # while W and W[-1] == 1:
    k -= 1
    while k >= 0 and W[k] == 1:
        ans += A[j] * 2
        j -= 1
        # W.pop()
        k -= 1
    
    for w in W[:k + 1]:
        ans += A[i] + A[j]
        j -= 1
        i += w - 1
    
    print(ans)

for _ in range(int(input())):
    solve()
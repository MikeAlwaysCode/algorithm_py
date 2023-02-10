import bisect
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
    arr.sort()
    ans = math.inf
    for i in range(1, n - 1):
        for j in range(i):
            right  = arr[i] * 2 - arr[j]
            j = bisect.bisect_left(arr, right, i + 1)
            if j < n:
                ans = min(ans, abs(right - arr[j]))
            if j - 1 > i:
                ans = min(ans, abs(right - arr[j - 1]))

    print(ans)

t = int(input())
for _ in range(t):
    solve()
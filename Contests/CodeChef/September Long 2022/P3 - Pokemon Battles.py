import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    A = ints()
    B = ints()

    arr = [(A[i], B[i]) for i in range(n)]
    # arr.sort(key = lambda x: x[0])
    arr.sort()

    ans = 1
    mx = arr[-1][1]
    for i in range(n-2, -1, -1):
        if arr[i][1] > mx:
            ans += 1
            mx = arr[i][1]

    print(ans)

t = int(input())
for _ in range(t):
    solve()
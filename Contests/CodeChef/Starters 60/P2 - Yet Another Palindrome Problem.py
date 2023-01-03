import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = int(input())
    arr = ints()

    ans = 0
    i, j = n // 2 - 1, (n + 1) // 2
    while i >= 0 and j < n:
        if arr[i] + ans > arr[j]:
            print(-1)
            return
        else:
            ans += arr[j] - arr[i] - ans
        i -= 1
        j += 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()
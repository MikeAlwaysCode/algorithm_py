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
    arr = ints()

    ans = 0
    l = r = 0
    while True:
        while r + 1 < n and ((r == l and arr[r+1] != arr[r]) or (arr[r+1] != arr[r] and arr[r+1] != arr[r-1])):
            r += 1
        # print(l, r)
        ans = max(ans, r - l + 1)
        if r == n - 1:
            break
        elif arr[r+1] == arr[r]:
            l = r = r + 1
        else:
            l = r
            r = r + 1
        # print(l, r)
    print(ans)
        

t = int(input())
for _ in range(t):
    solve()
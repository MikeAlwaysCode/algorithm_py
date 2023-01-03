import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n, k = map(int, input().split())
    arr = ints()
    nums = [0] * (2 * n + 1)
    mx = 0
    for a in arr:
        nums[a] += 1
        mx = max(mx, a)

    s = []
    mk = 0
    for i in range(1, 2 * n + 1):
        if not nums[i]:
            s.append(i)
        if i < mx:
            mk += 1
    
    ans1 = 0
    if mk >= k:
        for j in range(k):
            ans1 += mx - s[j]

    if mx < 2 * n:
        k -= 1
        mx = 2 * n
    ans2 = 0
    for j in range(k):
        ans2 += mx - s[j]

    print(max(ans1, ans2))

t = int(input())
for _ in range(t):
    solve()
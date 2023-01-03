import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n, k = map(int, input().split())
    s = input().strip()

    cnt1 = s.count("1")
    if cnt1 == n or cnt1 == 0:
        print("0" * n)
        return
    
    dis = [10 ** 10] * n
    pre0 = pre1 = -1
    for i in range(n):
        if s[i] == "1":
            pre1 = i
            if pre0 >= 0:
                dis[i] = i - pre0 + 1
        else:
            pre0 = i
            if pre1 >= 0:
                dis[i] = i - pre1

    pre0 = pre1 = -1
    for i in range(n-1, -1, -1):
        if s[i] == "1":
            pre1 = i
            if pre0 >= 0:
                dis[i] = min(dis[i], pre0 - i + 1)
        else:
            pre0 = i
            if pre1 >= 0:
                dis[i] = min(dis[i], pre1 - i)
    
    ans = ["0"] * n
    for i in range(n):
        if dis[i] <= k:
            ans[i] = str((k - dis[i] + 1) % 2)
    
    print("".join(ans))

t = int(input())
for _ in range(t):
    solve()
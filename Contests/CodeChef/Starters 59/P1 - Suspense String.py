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
    s = input().strip()
    ans = collections.deque()
    l, r = 0, n-1
    while l < r:
        if s[l] == "0":
            ans.appendleft("0")
        else:
            ans.append("1")
        if s[r] == "0":
            ans.append("0")
        else:
            ans.appendleft("1")
        l += 1
        r -= 1
    if l == r:
        if s[l] == "0":
            ans.appendleft("0")
        else:
            ans.append("1")
    
    print("".join(ans))

t = int(input())
for _ in range(t):
    solve()
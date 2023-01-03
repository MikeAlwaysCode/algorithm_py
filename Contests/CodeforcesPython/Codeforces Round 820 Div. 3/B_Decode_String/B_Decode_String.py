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
    
    i = n - 1
    ans = ""
    while i >= 0:
        if s[i] != "0":
            ans = chr(int(s[i]) + 96) + ans
            i -= 1
        else:
            ans = chr(int(s[i-2:i]) + 96) + ans
            i -= 3
    print(ans)

t = int(input())
for _ in range(t):
    solve()
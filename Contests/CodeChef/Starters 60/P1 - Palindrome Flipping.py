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
    s = input()
    if n & 1:
        print("YES")
        return
    i, j, cnt = 0, n - 1, 0
    while i < j:
        if s[i] != s[j]:
            cnt += 1
        i += 1
        j -= 1
    if cnt & 1:
        print("NO")
    else:
        print("YES")

t = int(input())
for _ in range(t):
    solve()
import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n, m = map(int, input().split())
    
    chk = True

    if n > m:
        print("No")
    elif n & 1:
        p = m - n + 1
        ans = [1] * (n)
        ans[0] = p
        print("Yes")
        print(*ans)
    elif not m & 1:
        p = (m - n + 2) // 2
        ans = [1] * (n)
        ans[0] = ans[1] = p
        print("Yes")
        print(*ans)
    else:
        print("No")

t = int(input())
for _ in range(t):
    solve()
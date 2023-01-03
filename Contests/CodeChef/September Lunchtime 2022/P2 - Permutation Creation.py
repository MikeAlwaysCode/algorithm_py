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
    if n < 4:
        print(-1)
        return
    
    if n == 4:
        print(3, 1, 4, 2)
        return
    
    ans = [0] * n
    for i in range(0, n, 2):
        ans[i] = i // 2 + 1
        if i < n - 1:
            ans[i+1] = (n + 1) // 2 + i // 2 + 1
    
    print(*ans)

t = int(input())
for _ in range(t):
    solve()
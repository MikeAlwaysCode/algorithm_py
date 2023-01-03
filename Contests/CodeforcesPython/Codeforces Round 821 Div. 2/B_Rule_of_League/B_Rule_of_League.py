import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def printQry(a, b) -> None:
    sa = str(a)
    sb = str(b)
    print(f"? {sa} {sb}", flush = True)

def printAns(ans) -> None:
    s = str(ans)
    print(f"! {s}", flush = True)

def solve() -> None:
    n, x, y = map(int, input().split())
    if x != 0 and y != 0:
        print(-1)
        return
    
    win = max(x, y)
    if win > n - 1 or win == 0 or (n - 1) % win != 0:
        print(-1)
        return

    ans = [0] * (n - 1)
    pre = 1
    for i in range(n - 1):
        if i > 0 and i % win == 0:
            pre = i + 2
        ans[i] = pre
    print(*ans)


t = int(input())
for _ in range(t):
    solve()
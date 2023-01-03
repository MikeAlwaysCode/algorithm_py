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
    n = int(input())
    arr = ints()

    ans = []
    
    if arr[0] != arr[n-1]:
        ans.append((1, n))
        if arr[0] % 2 == arr[n-1] % 2:
            arr[0] = arr[n-1]
        # else:
        #     ans[n-1] = ans[0]
    
    for i in range(1, n-1):
        if arr[i] != arr[0]:
            if (arr[i] + arr[0]) & 1:
                ans.append((1, i + 1))
                # arr[i] = arr[0]
            else:
                ans.append((i + 1, n))
                # arr[i] = arr[0]

    print(len(ans))
    for a in ans:
        print(*a)

t = int(input())
for _ in range(t):
    solve()
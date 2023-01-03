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
    n, m = map(int, input().split())
    islands = []
    for i in range(n):
        l, r = map(int, input().split())
        islands.append((l, r))
    arr = ints()
    
    dis = []
    for i in range(1, n):
        dis.append((islands[i][0] - islands[i-1][1], islands[i][1] - islands[i-1][0], i - 1))

    bridges = [(a, i + 1) for i, a in enumerate(arr)]

    dis.sort()
    bridges.sort()
    # print(dis)
    # print(bridges)
    ans = [0] * (n - 1)
    h = []
    j = 0
    for bridge in bridges:
        while j < n - 1 and dis[j][0] <= bridge[0]:
            heappush(h, (dis[j][1], dis[j][2]))
            j += 1
        
        if h:
            # p = heappop(h)
            p = h[0]
            # print(p)
            if p[0] < bridge[0]:
                break
            else:
                ans[p[1]] = bridge[1]
                heappop(h)
    
    if h or j < n - 1:
        print("No")
    else:
        print("Yes")
        print(*ans)
    

t = 1
for _ in range(t):
    solve()
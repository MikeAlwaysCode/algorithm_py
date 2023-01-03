import sys
import math
import collections
import random
from heapq import heapify, heappush, heappop
from functools import reduce

input = sys.stdin.readline
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n, q = map(int, input().split())
    arr = ints()
    dis = collections.defaultdict(int)
    ans = []
    for i in range(1, n):
        d = arr[i-1] - arr[i]
        if d > 0:
            dis[d] += 1
            ans.append(-d)

    heapify(ans)
    
    for _ in range(q):
        i, x = map(int, input().split())
        i -= 1
        pred = 0
        if i > 0:
            pred = arr[i-1] - arr[i]
            if pred > 0:
                dis[pred] -= 1

            pred = arr[i-1] - x
            if pred > 0:
                if dis[pred] == 0:
                    heappush(ans, -pred)
                dis[pred] += 1
        if i < n - 1:
            pred = arr[i] - arr[i+1]
            if pred > 0:
                dis[pred] -= 1

            pred = x - arr[i+1]
            if pred > 0:
                if dis[pred] == 0:
                    heappush(ans, -pred)
                dis[pred] += 1
        
        
        arr[i] = x

        while ans and dis[-ans[0]] <= 0:
            heappop(ans)

        if not ans:
            print(0)
        else:
            print(-ans[0])

t = int(input())
for _ in range(t):
    solve()
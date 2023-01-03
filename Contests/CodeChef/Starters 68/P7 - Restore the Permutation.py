import collections
import math
import random
import sys
from functools import reduce
from heapq import heapify, heappop, heappush

input = lambda: sys.stdin.readline().rstrip("\r\n")
ints = lambda: list(map(int, input().split()))

# MOD = 998244353
# MOD = 10 ** 9 + 7

def solve() -> None:
    n = int(input())
    arr = ints()

    cnt = [0] * n
    graph = [[] for _ in range(n)]
    pre = []
    for i, a in enumerate(arr):
        if a == -1:
            continue

        if a > i:
            print(-1)
            return

        if a:
            a -= 1
            graph[i].append(a)
            cnt[a] += 1
        
        while pre and pre[-1] > a:
            graph[pre[-1]].append(i)
            cnt[i] += 1
            pre.pop()
        
        pre.append(i)


    # print(cnt)
    # print(graph)
    
    h = [i for i in range(n) if cnt[i] == 0]
    heapify(h)
    ans = [0] * n
    k = 1
    while h:
        p = heappop(h)
        ans[p] = k
        k += 1

        for x in graph[p]:
            cnt[x] -= 1
            if cnt[x] == 0:
                heappush(h, x)

    if k <= n:
        print(-1)
    else:
        print(*ans)

t = int(input())
for _ in range(t):
    solve()